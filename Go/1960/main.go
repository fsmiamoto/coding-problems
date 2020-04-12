package main

import (
	"fmt"
)

type RomanNumeral struct {
	Value  int
	Symbol string
}

var ArabicToRoman = []RomanNumeral{
	{1000, "M"},
	{900, "CM"},
	{500, "D"},
	{400, "CD"},
	{100, "C"},
	{90, "XC"},
	{50, "L"},
	{40, "XL"},
	{10, "X"},
	{9, "IX"},
	{5, "V"},
	{4, "IV"},
	{1, "I"},
}

func ConvertToRoman(arabic int) string {
	var result string

	for _, num := range ArabicToRoman {
		for arabic >= num.Value {
			result += num.Symbol
			arabic -= num.Value
		}
	}

	return result
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	fmt.Println(ConvertToRoman(n))
}
