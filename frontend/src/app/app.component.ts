import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="theme-shell">
      <nav class="navbar navbar-expand-lg navbar-dark bg-primary-subtle">
        <div class="container-fluid">
          <a class="navbar-brand fw-bold" href="#">ClaimWise AI</a>
          <div class="d-flex gap-2">
            <button class="btn btn-outline-light btn-sm">Login</button>
            <button class="btn btn-light btn-sm">Register</button>
          </div>
        </div>
      </nav>

      <div class="container-fluid py-4">
        <div class="row g-3 mb-4">
          <div class="col-md-3" *ngFor="let stat of stats">
            <div class="glass-card">
              <h6>{{ stat.label }}</h6>
              <h2>{{ stat.value }}</h2>
            </div>
          </div>
        </div>

        <div class="row g-3">
          <div class="col-xl-7">
            <div class="glass-card">
              <div class="d-flex justify-content-between align-items-center mb-3">
                <h4>Claim Intake</h4>
                <span class="badge text-bg-light">Multimodal intake</span>
              </div>
              <form class="row g-3" (ngSubmit)="submitClaim()">
                <div class="col-md-6">
                  <input class="form-control" [(ngModel)]="claimantName" name="claimantName" placeholder="Claimant name">
                </div>
                <div class="col-md-6">
                  <input class="form-control" [(ngModel)]="policyNumber" name="policyNumber" placeholder="Policy number">
                </div>
                <div class="col-md-12">
                  <input class="form-control" [(ngModel)]="damageType" name="damageType" placeholder="Damage type">
                </div>
                <div class="col-md-12">
                  <textarea class="form-control" rows="3" [(ngModel)]="damageDescription" name="damageDescription" placeholder="Damage description"></textarea>
                </div>
                <div class="col-md-6">
                  <input type="file" class="form-control" aria-label="Damage image upload">
                </div>
                <div class="col-md-6">
                  <input type="file" class="form-control" aria-label="Supporting PDF upload">
                </div>
                <div class="col-12 d-flex gap-2 flex-wrap">
                  <button class="btn btn-primary" type="submit">Submit Claim</button>
                  <button class="btn btn-outline-light" type="button" (click)="simulateReview('approve')">Approve Demo</button>
                  <button class="btn btn-outline-light" type="button" (click)="simulateReview('reject')">Reject Demo</button>
                </div>
              </form>
            </div>
          </div>

          <div class="col-xl-5">
            <div class="glass-card">
              <h4 class="mb-3">AI Analysis</h4>
              <div class="mb-2"><strong>Claim ID:</strong> {{ activeClaimId }}</div>
              <div class="mb-2"><strong>Classification:</strong> {{ aiResult.classification }}</div>
              <div class="mb-2"><strong>Severity:</strong> {{ aiResult.severity }}</div>
              <div class="mb-2"><strong>Confidence:</strong> {{ aiResult.confidence }}%</div>
              <div class="mb-2"><strong>Estimated Cost:</strong> {{ aiResult.estimatedCost }}</div>
              <div class="mb-2"><strong>Fraud Risk:</strong> {{ aiResult.fraudRisk }}%</div>
              <div class="alert alert-warning mt-3 mb-0">
                Explainability: {{ aiResult.explanation }}
              </div>
            </div>
          </div>
        </div>

        <div class="row g-3 mt-1">
          <div class="col-lg-6">
            <div class="glass-card">
              <h4>Human Review Workflow</h4>
              <p class="mb-3">Current review state: <strong>{{ reviewState }}</strong></p>
              <div class="d-flex gap-2 flex-wrap">
                <button class="btn btn-success" (click)="simulateReview('approve')">Approve</button>
                <button class="btn btn-danger" (click)="simulateReview('reject')">Reject</button>
                <button class="btn btn-secondary" (click)="simulateReview('modify')">Modify</button>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="glass-card">
              <h4>ROI Calculator</h4>
              <p class="mb-1">Average reduction in claim cycle time: <strong>38%</strong></p>
              <p class="mb-1">Estimated annual savings: <strong>$2.4M</strong></p>
              <p class="mb-0">Coverage scope: multi-line insurance, auto, homeowners</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [
    `
      body {
        background: radial-gradient(circle at top, #0f2b46, #07121f);
        color: #f4f7fb;
        min-height: 100vh;
        font-family: Inter, Arial, sans-serif;
      }
      .theme-shell {
        min-height: 100vh;
        padding-bottom: 2rem;
      }
      .glass-card {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.14);
        backdrop-filter: blur(12px);
        border-radius: 18px;
        padding: 1.25rem;
        box-shadow: 0 10px 35px rgba(0,0,0,0.25);
      }
      .navbar {
        border-bottom: 1px solid rgba(255,255,255,0.12);
      }
      h2,
      h4,
      h6 {
        margin: 0;
      }
      .btn {
        border-radius: 999px;
      }
      textarea,
      input {
        background: rgba(255, 255, 255, 0.07);
        color: #f4f7fb;
        border: 1px solid rgba(255, 255, 255, 0.12);
      }
      textarea::placeholder,
      input::placeholder {
        color: #c7d5e9;
      }
    `,
  ],
})
export class AppComponent {
  claimantName = 'Ava Thompson';
  policyNumber = 'POL-2048';
  damageType = 'Rear bumper';
  damageDescription = 'Passenger-side rear impact with panel distortion and scratch segment.';
  activeClaimId = 'CLM-1001';
  reviewState = 'Pending Review';
  stats = [
    { label: 'Total Claims', value: '1,284' },
    { label: 'Pending Reviews', value: '186' },
    { label: 'Approved Claims', value: '842' },
    { label: 'AI Accuracy', value: '94%' },
  ];
  aiResult = {
    classification: 'Vehicle Damage',
    severity: 'Moderate',
    confidence: 93,
    estimatedCost: '$1,800 - $3,200',
    fraudRisk: 11,
    explanation:
      'Damaged region heatmap highlights rear passenger side with peak activation around panel impact and surface cracking.',
  };

  submitClaim(): void {
    this.activeClaimId = `CLM-${Math.floor(1000 + Math.random() * 9000)}`;
    this.reviewState = 'Pending Review';
    this.aiResult = {
      classification: 'Vehicle Damage',
      severity: 'Moderate',
      confidence: 93,
      estimatedCost: '$1,750 - $3,050',
      fraudRisk: 11,
      explanation: `AI assessed the ${this.damageType.toLowerCase()} claim for ${this.claimantName} and flagged a balanced severity profile with high confidence.`,
    };
  }

  simulateReview(action: 'approve' | 'reject' | 'modify'): void {
    if (action === 'approve') {
      this.reviewState = 'Approved';
      return;
    }
    if (action === 'reject') {
      this.reviewState = 'Rejected';
      return;
    }
    this.reviewState = 'Needs Correction';
  }
}
