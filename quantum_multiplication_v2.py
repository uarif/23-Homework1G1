import qiskit
import numpy as np

def quantum_multiplication(multiplicand, multiplier):
  """
  Performs quantum multiplication of two numbers.

  Args:
    multiplicand: The first number to multiply.
    multiplier: The second number to multiply.

  Returns:
    The product of the two numbers.
  """

  # Initialize the registers and quantum circuit.
  q = qiskit.QuantumRegister(4)
  c = qiskit.ClassicalRegister(4)
  circuit = qiskit.QuantumCircuit(q, c)

  # Encode the values on to the Operands.
  circuit.x(q[0])  # Set the multiplicand to |1>.
  circuit.x(q[1])  # Set the multiplier to |1>.

  # Add an Hadamard gate to each of the input qubits.
  circuit.h(q[0])
  circuit.h(q[1])
<<<<<<< HEAD:quantum_multiplication.py

  # Create the QFT multiplication circuit.
  qft_circuit = qiskit.assemble(qiskit.circuit.library.QFT(4))
    
  # Convert the QasmQobj object to a QuantumCircuit object.
  qft_circuit = qft_circuit.to_circuit()

  # Combine the two circuits.
  circuit += qft_circuit
=======
# Can you explain line # 40? what is it for ">>>>>>> pr/17:quantum_multiplication_v2.py"? This line I am talking about.
>>>>>>> pr/17:quantum_multiplication_v2.py

  # Create the QFT multiplication circuit.
  qft_circuit = qiskit.circuit.library.QFT(4)
    
  # Convert the QasmQobj object to a QuantumCircuit object.

  # Combine the two circuits.
  #circuit += qft_circuit
  circuit.compose(qft_circuit)
  # Measure the output qubits.
  circuit.measure(q, c)

  # Send the circuit to a backend device and get the results back.
  job = qiskit.execute(circuit, backend=qiskit.Aer.get_backend('qasm_simulator'))
  result = job.result()

  # The product is the binary representation of the measured state.
  product = format(result.get_counts().get('0000', 0), '04b')



  return int(product, 2)
