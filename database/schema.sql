CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'claims_officer',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS claims (
    id SERIAL PRIMARY KEY,
    claimant_name VARCHAR(255) NOT NULL,
    policy_number VARCHAR(120) NOT NULL,
    damage_type VARCHAR(120) NOT NULL,
    severity VARCHAR(50) NOT NULL,
    confidence_score DECIMAL(5,4),
    estimated_cost_range VARCHAR(120),
    fraud_risk_score DECIMAL(5,4),
    status VARCHAR(50) NOT NULL DEFAULT 'pending_review',
    reviewer_notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS decision_logs (
    id SERIAL PRIMARY KEY,
    claim_id INT REFERENCES claims(id),
    decision VARCHAR(50) NOT NULL,
    reviewer_notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_claims_status ON claims(status);
CREATE INDEX IF NOT EXISTS idx_claims_created_at ON claims(created_at);
