package main

import "fmt"

func main() {
	var numCases int
	fmt.Scanf("%d", &numCases)

	for i := 0; i < numCases; i++ {
		var sheldon, raj string
		fmt.Scanf("%s %s", &sheldon, &raj)

		fmt.Printf("Caso #%d: ", i+1)

		if sheldon == raj {
			fmt.Println("De novo!")
			continue
		}

		if ganhador(sheldon, raj) {
			fmt.Println("Bazinga!")
		} else {
			fmt.Println("Raj trapaceou!")
		}
	}

}

func ganhador(sheldon, raj string) (sheldonGanhou bool) {

	switch sheldon {
	case "pedra":
		if raj == "lagarto" || raj == "tesoura" {
			return true
		}
	case "tesoura":
		if raj == "papel" || raj == "lagarto" {
			return true
		}
	case "papel":
		if raj == "pedra" || raj == "Spock" {
			return true
		}
	case "lagarto":
		if raj == "papel" || raj == "Spock" {
			return true
		}
	case "Spock":
		if raj == "pedra" || raj == "tesoura" {
			return true
		}
	}
	return false
}
