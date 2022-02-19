package main

import "fmt"

func main() {
	datas := make([]int, 2, 2)

	for index, _ := range datas {
		d, h, m, s := 0, 0, 0, 0
		fmt.Scanf("Dia %d", &d)
		fmt.Scanf("%d : %d : %d", &h, &m, &s)
		datas[index] = d*86400 + h*3600 + m*60 + s
	}

	diff := datas[1] - datas[0]

	dias, resto := divmod(diff, 86400)
	horas, resto := divmod(resto, 3600)
	mins, segs := divmod(resto, 60)

	// Show result
	fmt.Printf("%d dia(s)\n", dias)
	fmt.Printf("%d hora(s)\n", horas)
	fmt.Printf("%d minuto(s)\n", mins)
	fmt.Printf("%d segundo(s)\n", segs)
}

func divmod(num, den int) (quoc, resto int) {
	quoc = num / den
	resto = num % den
	return
}
