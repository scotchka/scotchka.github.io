Determining endianness
======================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

"Endianness" is how the digits in a number are arranged.
Humans write numbers from the most significant digit to the least significant
digit. This order is called "big-endian" -- big end first. The reverse is called
"little-endian".

In computer memory, a number is represented as a consecutive sequence of bits. A **long** integer takes
up 8 bytes (64 bits), for example.
This raises a question: does the lowest address byte represent the most significant or the least
sigificant digits of the number?

To decide this, we can run a short C program:

.. literalinclude:: endian.c
    :caption: endian.c

For simplicity, we initialize an `unsigned long` and assign its address
to a pointer to an `unsigned char`. This means that if we add an integer to the pointer,
the resulting address will advance by that many bytes. Simply put, we print the base 256
representation of the long integer.

The output on an Intel x86 machine is:

.. parsed-literal::

    $ gcc endian.c
    $ ./a.out
    0 0 1 0 0 0 0 0

The third and only nonzero byte is 1. This establishes that the integer is stored in memory in
little-endian fashion.
