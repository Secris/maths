#!/usr/bin/env lua
--[[
--Each number is obtained from the previous iteration.
--Start with x
--If x is odd 3x+1
--If x is even x/2
--Repeat until you reach 1
--
--The question trying to be solved is:
--Will all positive integers eventually reach 1?
--Do all numbers result in the same 4, 2, 1 loop?
]]--

local start_num
local good = "no"
local collatz = ""
local current_value = 0

repeat
    io.write("Please input a starting number: ")
    start_num = io.read()
    start_num = tonumber(start_num)
    if type(start_num) == "number" then
        good = "yes"
    else
        print("Input was not a number")
    end
until good == "yes"

current_value = start_num
repeat 
    if current_value % 2 == 0 then
        -- current is even
        current_value = current_value / 2
    else
        -- current is odd
        current_value = (3 * current_value) + 1
    end
    collatz = collatz .. current_value .. " "
until current_value == 1

print("num: ", start_num)
print("collatz: ", collatz)
