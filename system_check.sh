#!/bin/bash

# system_check.sh
# A script to interact with PIT Agent Framework endpoints with proper logging and colors.

# Exit immediately if a command exits with a non-zero status.
set -e

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to make API calls and handle responses
make_request() {
    local method=$1
    local url=$2
    local data=$3

    if [ "$method" == "GET" ]; then
        response=$(curl -s -X GET "$url")
    elif [ "$method" == "POST" ]; then
        response=$(curl -s -X POST "$url" -H "Content-Type: application/json" -d "$data")
    else
        log_error "Unsupported HTTP method: $method"
        exit 1
    fi

    echo "$response"
}

# Start of the script
clear
log_info "Starting PIT Agent Framework System Check..."
sleep 2

# Base URL of the Flask API
BASE_URL="http://127.0.0.1:5000/api"

# Step 1: Create Agent 1
clear
log_info "Step 1: Creating Agent 'agent_1'..."
AGENT_1_ID="agent_1"
CREATE_AGENT_1_PAYLOAD=$(jq -n --arg agent_id "$AGENT_1_ID" '{agent_id: $agent_id}')
CREATE_AGENT_1_RESPONSE=$(make_request "POST" "$BASE_URL/agents/create" "$CREATE_AGENT_1_PAYLOAD")

# Check if creation was successful
if echo "$CREATE_AGENT_1_RESPONSE" | jq -e '.message' > /dev/null; then
    MESSAGE=$(echo "$CREATE_AGENT_1_RESPONSE" | jq -r '.message')
    log_success "$MESSAGE"
else
    log_error "Failed to create Agent 'agent_1'. Response: $CREATE_AGENT_1_RESPONSE"
    exit 1
fi

sleep 2

# Step 2: Create Agent 2
clear
log_info "Step 2: Creating Agent 'agent_2'..."
AGENT_2_ID="agent_2"
CREATE_AGENT_2_PAYLOAD=$(jq -n --arg agent_id "$AGENT_2_ID" '{agent_id: $agent_id}')
CREATE_AGENT_2_RESPONSE=$(make_request "POST" "$BASE_URL/agents/create" "$CREATE_AGENT_2_PAYLOAD")

# Check if creation was successful
if echo "$CREATE_AGENT_2_RESPONSE" | jq -e '.message' > /dev/null; then
    MESSAGE=$(echo "$CREATE_AGENT_2_RESPONSE" | jq -r '.message')
    log_success "$MESSAGE"
else
    log_error "Failed to create Agent 'agent_2'. Response: $CREATE_AGENT_2_RESPONSE"
    exit 1
fi

sleep 2

# Step 3: Mint a Token for Agent 1
clear
log_info "Step 3: Minting a Token for 'agent_1'..."
MINT_TOKEN_PAYLOAD=$(jq -n \
    --arg agent_id "$AGENT_1_ID" \
    --argjson token_data '{"amount": 100, "purpose": "Utility token", "condition": "time_lock"}' \
    '{agent_id: $agent_id, token_data: $token_data}')
MINT_TOKEN_RESPONSE=$(make_request "POST" "$BASE_URL/blockchain/add_token" "$MINT_TOKEN_PAYLOAD")

# Check if minting was successful
if echo "$MINT_TOKEN_RESPONSE" | jq -e '.block.id' > /dev/null; then
#    TOKEN_ID=$(echo "$MINT_TOKEN_RESPONSE" | jq -r '.block.id')
    TOKEN_ID=$(echo "$MINT_TOKEN_RESPONSE" | jq -r '.block.hash')
    log_success "Token minted successfully with Token ID: $TOKEN_ID:"
else
    log_error "Failed to mint token for 'agent_1'. Response: $MINT_TOKEN_RESPONSE"
    exit 1
fi

sleep 2


# Step 4: Validate Token Conditions
clear
log_info "Step 4: Validating Token Conditions for Token ID '$TOKEN_ID'..."
VALIDATE_URL="$BASE_URL/blockchain/validate?token_id=$TOKEN_ID"
VALIDATE_RESPONSE=$(make_request "GET" "$VALIDATE_URL")

# Check validation result
if echo "$VALIDATE_RESPONSE" | jq -e '.is_valid' > /dev/null; then
    IS_VALID=$(echo "$VALIDATE_RESPONSE" | jq -r '.is_valid')
    if [ "$IS_VALID" == "true" ]; then
        log_success "Token ID '$TOKEN_ID' is valid."
    else
        log_warning "Token ID '$TOKEN_ID' is NOT valid due to unmet conditions."
    fi
else
    log_error "Failed to validate token. Response: $VALIDATE_RESPONSE"
    exit 1
fi
# Step 5: Validate the Blockchain
clear
log_info "Step 5: Validating the Blockchain..."
VALIDATE_BLOCKCHAIN_URL="$BASE_URL/blockchain/validate"
VALIDATE_BLOCKCHAIN_RESPONSE=$(make_request "GET" "$VALIDATE_BLOCKCHAIN_URL")

# Check blockchain validity
IS_BLOCKCHAIN_VALID=$(echo "$VALIDATE_BLOCKCHAIN_RESPONSE" | jq -r '.is_valid')
if [ "$IS_BLOCKCHAIN_VALID" == "true" ]; then
    log_success "Blockchain is valid and intact."
else
    log_error "Blockchain validation failed. The chain is compromised."
    exit 1
fi

sleep 2

# Step 6: Retrieve All Agents and Their Tokens
clear
log_info "Step 6: Retrieving All Agents and Their Tokens..."
GET_AGENTS_URL="$BASE_URL/agents/"
GET_AGENTS_RESPONSE=$(make_request "GET" "$GET_AGENTS_URL")

# Display agents and their tokens
if echo "$GET_AGENTS_RESPONSE" | jq -e '.agents' > /dev/null; then
    AGENTS=$(echo "$GET_AGENTS_RESPONSE" | jq -r '.agents[] | "Agent ID: \(.agent_id)\nTokens: \(.tokens)"')
    echo -e "${GREEN}$AGENTS${NC}"
else
    log_error "Failed to retrieve agents. Response: $GET_AGENTS_RESPONSE"
    exit 1
fi