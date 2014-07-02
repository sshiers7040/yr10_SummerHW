#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
Computers can only store 2 values, 1 and 0, representing high and low voltage.
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
10010011
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
b = 11 * 16 = 176
176 + 5 = 181

181
```
###4 - Here is a function written is **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
A list.
```

(b) What type of data is returned by this function? **(1 mark)**
```
Boolean.
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
7
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
An error in the code so that it is not understood by the language and does not run.
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
On line 4 tot is assigned to nums[x], where as nums[x] should be added to it.
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
A runtime error is an error that cause the program to crash when running because it can not perform a task, for example dividing by 0. A runtime error involving mathematics is also called a mathematical error.
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```

numbers #This is a list of numbers
largest <- numbers[1] #To hold the largest number so far; starting with the first value in numbers
FOR x <- 2 TO len(numbers) #For all numbers in numbers; numbers[1] has already been dealt with, so we start with x <- 2
	IF largest < numbers[x] THEN #If the next value from numbers is larger than the largest so far
		largest <- numbers[x] #Make largest equal to that value
	ENDIF
ENDFOR
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe: All the clients, resources and servers are connected to one cable known as the bus. All the information is transmitted down this until it reaches its destination, where it is processed. Terminators at each end of the bus stop the information from being constantly reflected backa long the us.

Advantages: A short amount of cable is used, which makes it cheap and easy to install.

Disadvantages: If the bus fails, the whoole network will fail.
	As more workstations are added, the netwrok becomes slower due to data collisions.
	The data can be seen by all workstations, so there is a security risk.
```

**Ring Topology (6 marks)**
```
Describe: Each device in the network is connected to two other devices, and this forms a ring where data is transferred in one direction to the next device until the destination device recieves it.

Advantages: Data has the potential to be transferred quickly, as the data only travels in one direction meaning that there will not be any data collisions.

Disadvantages: Data has the potential to be transferred slowly, as it could have to pass through many devices before it reaches its destination.
	Connections are shared between all devices, so there is a security risk.
	One faulty device or connection can fail the whole network.
```

**Star Topology (6 marks)**
```
Describe: All devices in the network are seperately connected to a switch, hub or router, each needing their own cable or connection.

Advantages: They are reliable, as if one connection or device fails, it will not affect the rest of the network.
	They have a high performing rate as data collisions can not occur.

Disadvantages: It cam be expensive as lots of cables/connections are needed, and a central hub/switch/router has to be purhcased/made.
	The whole network can still fail if the central device fails.
```
