
# Devlog

## Tuesday 27/10/2026

### Goals
- Create a directory for documents to be stored
- Have the files in the doc directory split into chunks and embedded, then store those vectors in vector db

### Changes
- created directory for files to be stores and read from
- added ingestion loop which takes in one string of entire file contents, chunks it (1000 char chunk with 200 char overflow) and then embeds each of those chunk strings into a vector and then inserts a row to the documents table containing the vector and the chunk/file metadata

### Issues
- deciding which chunking strategy to use. it was pretty overwhelming reading all the different chunking strategies and their ideal use cases. instead of finding out what is the best and implementing that i decided to just start small and use a simple chunking method. 

### Other notes
- ngl this entire project has a lot of different architectural decisions that have their own trade offs. its quite overwhelming and i sometimes found myself going too deep into rabbit holes trying to find the most accurate or most performant solution, but i instead found something better. if i just implement the most naive solution or pick the simplest option, i get a working prototype. i can then look at how to improve that and iteratively improve on it. feels like a lot of things in computer science and engineering have super thought out and effective solutions already but its not realistic for me (and juniors alike) to immediately jump to them without doing the hard thinking that made it possible to get there.
- i learnt a lot today and plan on fixing up the query results output in the terminal so its more readable
- also plan on fixing up the chunking method so its sentence aware instead of just character based as a lot of the chunks started and stopped at awkward positions in the text. i also read an aritcle on better chunking methods which i might try out