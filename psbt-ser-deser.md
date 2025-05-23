### PSBT Unserialization

* The PSBT comes in the `DataStream` format:
 https://github.com/bitcoin/bitcoin/blob/baa848b8d38187ce6b24a57cfadf1ea180209711/src/streams.h#L146

* The `>>` operator is overloaded for the stream class that is called whenever a
stream is read using `>>`.
 https://github.com/bitcoin/bitcoin/blob/baa848b8d38187ce6b24a57cfadf1ea180209711/src/streams.h#L265-L269

* This^ internally calls the `Unserialize` function that is overloaded for calls
with various datatypes in the `src/serialize.h` file. The object the stream data
is read into is passed as the second argument, which is overloaded.

* For the PSBT key case, the data is read into a vector of chars that ends up 
this overloaded `Unserialize` function:
 https://github.com/bitcoin/bitcoin/blob/baa848b8d38187ce6b24a57cfadf1ea180209711/src/serialize.h#L865-L881

* The `ReadCompactSize` function handles reading sizes of data of 1, 2, 4 and 8 bytes:
 https://github.com/bitcoin/bitcoin/blob/master/src/serialize.h#L339
** The `ReadCompactSize` function returns the actual size (after the compact 
size encoding) that needs to be read. 

* The `ser_readdata*` functions read the data from the passed stream that ends up
calling the `read` function of `DataStream` that writes the read data in the passed
destination using `memcpy` & also moves along the `m_read_pos` member of the stream.
 https://github.com/bitcoin/bitcoin/blob/master/src/streams.h#L218-L234
** After reading if the cursor reaches the end of the stream, then the internal
members of the stream such as `vch` & `m_read_pos` are cleared.

* Notably, the `ser_readdata*` functions read the data in a dummy object internally
 as these functions are not passed a reference to read the data into.

* The `Unserialize` function reads the "actual" vector data from the stream later
after reading the compact size because the vectors are usually prefixed with their
lengths to let the reader know how much to read.
 https://github.com/bitcoin/bitcoin/blob/baa848b8d38187ce6b24a57cfadf1ea180209711/src/serialize.h#L872-L877 

* Sometimes, the stream is a `SpanReader` object instead of `DataStream` like in
case of `skey`. In this case, the `read` function boils down to the `SpanReader`
one: https://github.com/bitcoin/bitcoin/blob/baa848b8d38187ce6b24a57cfadf1ea180209711/src/streams.h#L121-L133

* Interestingly, for this the span keeps getting shortened everytime data is read
off of it, which is maintained in the `m_data` member.
 https://github.com/bitcoin/bitcoin/blob/baa848b8d38187ce6b24a57cfadf1ea180209711/src/streams.h#L132C9-L132C15
