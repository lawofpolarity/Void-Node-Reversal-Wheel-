# Void Node Reversal Wheel (VNRW)

> **Legacy symbolic/operator research candidate. Historical source preserved; engineering claims are not inherited as facts.**

The original repository proposed twelve "void" or inversion primitives and mapped them directly onto software, hardware, quantum, security, medical and media applications. The historical README is preserved unchanged at [docs/LEGACY_VNRW_SOURCE.md](docs/LEGACY_VNRW_SOURCE.md).

The constitutional reconstruction asks a narrower question:

> Can the historical void vocabulary be translated into mathematically defined operations on state—reset, rollback, cancellation, projection to baseline, pre-initialization and erasure—without claiming unsupported physical effects?

## Current result

**Yes, partially.** A reusable state-transition vocabulary survives. The universal physical claims do not.

[
	ext{state }x
ightarrow
{	ext{restore},	ext{reset},	ext{cancel},	ext{erase},	ext{hold},	ext{preinitialize}}
]

These operations are not equivalent. A central contribution of the reconstruction is to prevent "void" from collapsing them into one operation.

## Status

| Field | State |
|---|---|
| Historical artifact | preserved |
| Canonical Σ13 identity | unresolved |
| 12 historical primitives | retained as source labels |
| Formal operator algebra | candidate only |
| Pair proofs/chirality | absent |
| PTE/RSCS/SS/lag | uncomputed |
| RFC | unqualified |
| G1–G4 | open |
| Physical performance claims | not established |
| Canonical admission | NO |

## Repository map

- [Historical README](docs/LEGACY_VNRW_SOURCE.md)
- [Constitutional status](CONSTITUTIONAL_STATUS.md)
- [Claim ledger](CLAIM_LEDGER.md)
- [Recoverable research value](RECOVERABLE_RESEARCH_VALUE.md)
- [Operator reconstruction](OPERATOR_RECONSTRUCTION.md)
- [Executable finite-state reference](src/reversal_operators.py)
- [Software contracts](tests/test_reversal_operators.py)

## Non-inference boundary

`x -> 0` is not necessarily rollback.  
Rollback is not secure erasure.  
Logical negation is not data sanitization.  
Zero software activity is not zero physical power.  
Restoring a phase variable is not qubit reset.  
Setting a mass variable to zero does not remove physical mass.

The reconstructed VNRW is therefore an **operator-semantics research artifact**, not a universal physical inversion engine.
