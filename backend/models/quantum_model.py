import pennylane as qml
import numpy as np

def quantum_circuit(weights):
    dev = qml.device("default.qubit", wires=1)

    @qml.qnode(dev)
    def circuit(params):
        qml.RX(params[0], wires=0)
        qml.RY(params[1], wires=0)
        return qml.expval(qml.PauliZ(0))

    return circuit(weights)

def predict(data):
    weights = np.random.rand(2)
    result = quantum_circuit(weights)
    return {"quantum_result": result}
