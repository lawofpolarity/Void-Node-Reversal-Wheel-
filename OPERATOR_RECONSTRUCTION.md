# VNRW Operator Reconstruction v0.1

## Typed state space
Let a system have states (X), distinguished initialization state (x_0), optional checkpoint (c), and optional absorbing/deleted marker (⊥).

## Operators

### RESTORE
[
R_c:X\to X,quad R_c(x)=c.
]
Requires a valid checkpoint. It does not reconstruct a checkpoint that was never stored.

### RESET
[
Z:X\to X,quad Z(x)=x_0.
]
Reset discards distinctions among prior states; it is generally many-to-one.

### CANCEL
Where an algebraic inverse exists:
[
C(x)=x+(-x)=0.
]
Cancellation concerns value, not storage remanence.

### DELETE
[
D:X\to X\cup\{⊥\},quad D(x)=⊥.
]
This models logical unavailability only. It makes no physical sanitization claim.

### HOLD
[
H(x)=x.
]
Identity transition over a declared interval. It makes no energy claim.

### PREINITIALIZE
Introduce PREINIT in a state machine:
[
PREINIT\rightarrow INIT\rightarrow RUN.
]

## Information-loss witness
RESET and DELETE are typically many-to-one. If (x_1\ne x_2) but (Z(x_1)=Z(x_2)=x_0), prior-state information is lost by the projection. Recoverability therefore requires auxiliary state such as a checkpoint/log.

## Reversal proof obligations
Any future reversal claim must declare:
1. domain/codomain;
2. target state;
3. preconditions;
4. whether the operator is injective;
5. information lost;
6. auxiliary state needed for inversion;
7. termination condition;
8. whether the claim is logical, numerical or physical.

This protocol is the strongest surviving mathematical contribution of VNRW.
