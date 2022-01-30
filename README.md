Our project is based on the implementation of the  **Ekert protocol**. It includes the code for an interface for secure communication line between the users *Alice& and *Bob* by having shared key between them.

The Ekert protocol is an **entanglement-based protocol** that uses maximally entangled Bell states emitted by a common source and distributed between Alice and Bob. If third person *Eve* interacts with the state shared between Alice and Bob, it will not remain maximally entangled anymore, and *Alice* and *Bob* can check how much Eve has interacted with the state. We have implemented the algorithm using **Qiskit** integrated with **Quantum Inspire** on the **qBriad** platform. The classical communication channel between Alice and Bob has been established using the **Twitter API** through the tweepy python module.
Alice and Bob share the basis for measurement over the interface. The code then runs on a Quantum Computer, wherein entangled qubits pair are formed and applies the appropriate basis, and finally, we obtain the key by looking for a shared basis between Alice and Bob.

Team Experience: 
The MIT iQuHACK 2022 has been an incredible experience. 
Our team was assigned the QuTech Division, and we worked on the Quantum Key Distribution Challenge. We read about QKD and the algorithms in QKD that we could implement. We implemented the Ekert Protocol using the Quantum inspire platform and used Tweepy as the channel for sending messages. 
We gained abundant knowledge, worked together and formed good bonds with each other as a team as we sailed through the challenge. We helped each other whenever we got stuck. We would like to especially thank our mentors, Tumi and Richard Versluis, for their invaluable suggestions and clarifications of our doubts throughout the event. We are thankful to the entire organizing team for such a great arrangement. Despite the entirely virtual program, we were never left out from great networking and interacting with each other.



References:

1)https://www.cse.wustl.edu/~jain/cse571-07/ftp/quantum/

2)https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
