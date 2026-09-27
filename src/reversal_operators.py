"""Finite-state reference for reconstructed VNRW operator semantics.

Logical model only. No physical erasure, energy, quantum, mass, or security claims.
"""
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Optional

class Phase(Enum):
    PREINIT=auto(); INIT=auto(); RUN=auto(); HELD=auto(); DELETED=auto()

@dataclass(frozen=True)
class State:
    value: Any
    phase: Phase=Phase.RUN

@dataclass(frozen=True)
class Transition:
    before: State
    after: State
    operator: str
    information_lost: bool

def restore(state: State, checkpoint: State) -> Transition:
    return Transition(state,checkpoint,"RESTORE",state != checkpoint)

def reset(state: State, initial: State) -> Transition:
    return Transition(state,initial,"RESET",state != initial)

def cancel_numeric(value):
    """Algebraic cancellation only; not storage erasure."""
    return value + (-value)

def logical_delete(state: State) -> Transition:
    deleted=State(None,Phase.DELETED)
    return Transition(state,deleted,"DELETE",state != deleted)

def hold(state: State) -> Transition:
    return Transition(state,state,"HOLD",False)

def preinitialize(value: Optional[Any]=None) -> State:
    return State(value,Phase.PREINIT)

def initialize(state: State, initial_value: Any) -> Transition:
    if state.phase is not Phase.PREINIT:
        raise ValueError("initialize requires PREINIT")
    return Transition(state,State(initial_value,Phase.INIT),"INITIALIZE",state.value != initial_value)
