# Active Context

## Current Focus
- Review and documentation of charge density prediction methods
- Detailed analysis of SCDP (Spherical Channel Density Prediction) architecture

## Recent Changes
- Added detailed mathematical formulation of SCDP's tensor product operation
- Documented equivariance guarantees and implementation details

## SCDP Architecture Summary

### Core Components
1. Virtual Nodes
   - Placed at bond midpoints
   - Use oxygen basis functions
   - SE(3)-equivariant placement

2. Even-tempered Gaussian Basis
   - Mathematical form: αₖ = α · βᵏ for k = 0,1,2,...,Nₗ
   - Controlled expressivity through β parameter
   - Learnable scaling factors sᵢⱼ ∈ (0.5, 2.0)

3. eSCN Backbone
   - Complexity: O(L³) vs O(L⁶) for tensor products
   - Features: Multi-channel spherical harmonics
   - Example configuration: 128×0e + 128×1o + 128×2e + 128×3o

### Tensor Product Operation
1. Mathematical Definition
   ```latex
   (U^(ℓ₁,p₁) ⊗ V^(ℓ₂,p₂))^(ℓₒ,pₒ)_cmₒ = ∑∑ C^(ℓₒ,mₒ)_(ℓ₁,m₁)(ℓ₂,m₂) U^(ℓ₁,p₁)_cm₁ V^(ℓ₂,p₂)_cm₂
   ```
   where:
   - |ℓ₁ - ℓ₂| ≤ ℓₒ ≤ |ℓ₁ + ℓ₂|
   - pₒ = p₁p₂
   - C^(ℓₒ,mₒ)_(ℓ₁,m₁)(ℓ₂,m₂) are Clebsch-Gordan coefficients

2. Key Properties
   - Preserves SO(3) equivariance
   - Combines features of different angular momenta
   - Output channels determined by tensor product rules

3. Implementation Details
   - Pre-computed Clebsch-Gordan coefficients
   - Efficient sparse tensor operations
   - Channel-wise feature combination

### Performance Metrics
- NMAE: 0.178% on QM9 test set
- 31.7x faster than ChargE3Net
- Flexible accuracy-efficiency trade-off

## Next Steps
- Review other charge density prediction methods
- Compare performance metrics across different approaches
- Document implementation details and best practices

## Active Decisions
- Using eSCN as backbone for its efficient tensor product implementation
- Implementing two-stage training for stability with scaling factors
- Balancing model capacity and efficiency through β parameter tuning

## Current Considerations
- Slide generation methodology
- Template standardization
- Content organization
- Version control strategy
- Documentation maintenance 