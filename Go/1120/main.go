/* 1120 -  Revisão de Contrato  */
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var faultyDigit, ammount string
	for {
		fmt.Scanf("%s %s", &faultyDigit, &ammount)

		if faultyDigit == "0" && ammount == "0" {
			break
		}

		if hasFaultyDigit := strings.Contains(ammount, faultyDigit); !hasFaultyDigit {
			fmt.Println(ammount)
			continue
		}

		filteredAmmount := strings.ReplaceAll(ammount, faultyDigit, "")

		if filteredAmmount != "" {
			ammountAsInt, _ := strconv.Atoi(filteredAmmount)
			fmt.Println(ammountAsInt)
			continue
		}

		fmt.Println(0)
	}
}
