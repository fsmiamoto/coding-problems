package main

import "fmt"

func main() {
	var diaEntrega, diaFinal int

	fmt.Scanf("%d %d", &diaEntrega, &diaFinal)

	if diaFinal >= 24 || diaEntrega > diaFinal {
		fmt.Println("Eu odeio a professora!")
		return
	}

	if diaFinal-diaEntrega >= 3 {
		fmt.Println("Muito bem! Apresenta antes do Natal!")
		return
	}

	fmt.Println("Parece o trabalho do meu filho!")

	if diaEntrega+2 >= 24 {
		fmt.Println("Fail! Entao eh nataaaaal!")
	} else {
		fmt.Println("TCC Apresentado!")
	}

}
