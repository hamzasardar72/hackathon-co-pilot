import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
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
          <div class="col-md-3"><div class="glass-card"><h6>Total Claims</h6><h2>1,284</h2></div></div>
          <div class="col-md-3"><div class="glass-card"><h6>Pending Reviews</h6><h2>186</h2></div></div>
          <div class="col-md-3"><div class="glass-card"><h6>Approved Claims</h6><h2>842</h2></div></div>
          <div class="col-md-3"><div class="glass-card"><h6>AI Accuracy</h6><h2>94%</h2></div></div>
        </div>

        <div class="row g-3">
          <div class="col-xl-7">
            <div class="glass-card">
              <h4 class="mb-3">Claim Intake</h4>
              <form class="row g-3">
                <div class="col-md-6"><input class="form-control" placeholder="Claimant name"></div>
                <div class="col-md-6"><input class="form-control" placeholder="Policy number"></div>
                <div class="col-md-12"><input class="form-control" placeholder="Damage description"></div>
                <div class="col-md-6"><input type="file" class="form-control"></div>
                <div class="col-md-6"><input type="file" class="form-control"></div>
                <button class="btn btn-primary w-auto">Submit Claim</button>
              </form>
            </div>
          </div>

          <div class="col-xl-5">
            <div class="glass-card">
              <h4 class="mb-3">AI Analysis</h4>
              <div class="mb-2"><strong>Classification:</strong> Vehicle Damage</div>
              <div class="mb-2"><strong>Severity:</strong> Moderate</div>
              <div class="mb-2"><strong>Confidence:</strong> 93%</div>
              <div class="mb-2"><strong>Estimated Cost:</strong> $1,800 - $3,200</div>
              <div class="mb-2"><strong>Fraud Risk:</strong> 11%</div>
              <div class="alert alert-warning">Explainability: damaged region heatmap highlights rear passenger side with strong activation around panel impact and surface cracking.</div>
            </div>
          </div>
        </div>

        <div class="row g-3 mt-1">
          <div class="col-lg-6"><div class="glass-card"><h4>Human Review Workflow</h4><button class="btn btn-success me-2">Approve</button><button class="btn btn-danger me-2">Reject</button><button class="btn btn-secondary">Modify</button></div></div>
          <div class="col-lg-6"><div class="glass-card"><h4>ROI Calculator</h4><p>Average reduction in claim cycle time: 38%</p><p>Estimated annual savings: $2.4M</p></div></div>
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
      h2, h4, h6 { margin: 0; }
      .btn { border-radius: 999px; }
    `,
  ],
})
export class AppComponent {}
