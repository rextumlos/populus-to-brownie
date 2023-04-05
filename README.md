# Populus? CHANGE TO BROWNIE

## This repository is for using brownie instead of populus from the book of "Hands-On Blockchain for Python Developers" for Chapter 06.

## How to install?
Visit this link: [https://chain.link/bootcamp/brownie-setup-instructions]

You can ignore installing Metamask. Credits to Chainlink!

Also, `pip install vyper` on your virtual environment.

__For the version of Python, do not use `version 11` and above because I was having errors on installing brownie. Use any version from 9 to 10, but not 11.__

## Tutorials on Brownie (Chainlink)
1. [Introduction to Brownie](https://youtu.be/JrYdDkpOzyQ)
2. [Testing with Brownie](https://youtu.be/uR3VKVQtYhQ)

## More information I encountered

### Compiling with Vyper
When compiling with vyper files for the first time. Include `#@version ^0.2.0` at the top of your vyper script. It is called `pragma` and Brownie uses this to install its own vyper compiler.

After the brownie's vyper compiler is installed, __take note of the `version` of the vyper compiler that is installed by brownie__, and change the `pragma `version on your vyper script by setting it the version of the vyper compiler. For example, in my case, `#@version 0.2.16`.

### For deploying to Ganache (GUI) software
Enter the command: `brownie add networks Ethereum ganache-local host=your_ganache_local_network chainid=your_ganache_network_id`

For example: `brownie add networks Ethereum ganache-local host=http://127.0.0.1:7545 chainid=5777`

Then deploy your contracts using: `brownie run your_deploy_script.py --networks ganache-local`
