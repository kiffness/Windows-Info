# Windows-Info
Script to get info about windows computers and save in sqlite3 database. The info it will collect is Computer name, Logged in user,
Windows version, Cpu brand and type, Ram capacity and the amount of ram slots on the motherboard expandoing on these I added last logon date and the ipaddress of the remote
Computer.
## Why?
I was tasked with doing a windows 10 refresh on all the computers in the company where I work and instead of gathering all the information I
need about the computers by walking to each one. I can now remotley connect to a computer using its computer name get the info I need and 
save it in a database from the comfort of my chair
## What does it do
First the powershell script gathers the information I need from the remote computers and saves it in a text file, Then my Python program
will read in that text file and save the information to a sqlite databse. I gave the program a simple command line ui just so i could add
some extra functionality like viewing the text file but not writing it to the database and I will add to it in the future
## Getting started 
To use this script you need to have **Python 3** installed on your pc, you then need make a sqlite database with all the parameters that
you will be passing in to it one table should do but you can make multiple tables if you want and just change up the code a bit. 
Run the script from the command line or using a bat file by saving this in it @py.exe F:\path\to\your\script.py %*.
## MIT Licence

copyright (c) 2019 Kyle Taylor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
