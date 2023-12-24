package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var totalColors = map[string]int{
	"red":   12,
	"blue":  14,
	"green": 13,
}

func main() {
	lines := getLinesFromFile("./input.txt")
	validGames := getValidGames(lines)
	calculateAndPrintSum(validGames)
}

func getLinesFromFile(filename string) []string {
	file, fileError := os.Open(filename)
	if fileError != nil {
		log.Fatal(fileError)
	}

	defer file.Close()
	scanner := bufio.NewScanner(file)
	var lines []string

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func getValidGames(lines []string) []int {
	var validGames []int
	for gameNmbr, line := range lines {
		gameInformation := strings.Split(line, ":")
		sets := strings.Split(gameInformation[1], ";")

		isGameValid := true
		for _, set := range sets {
			state := true
			numOfEachColoredCubes := strings.Split(set, ",")

			for _, colorCount := range numOfEachColoredCubes {
				countAndColor := strings.Split(colorCount, " ")
				countAsInt, _ := strconv.Atoi(countAndColor[1])

				if !isColorCountValid(countAsInt, countAndColor[2]) {
					isGameValid = false
					state = false
					break
				}
			}
			if !state {
				break
			}
		}
		if isGameValid {
			validGames = append(validGames, gameNmbr+1)
		}
	}
	return validGames
}

func isColorCountValid(count int, color string) bool {
	return count <= totalColors[color]
}

func calculateAndPrintSum(validGames []int) {
	sum := 0
	for _, game := range validGames {
		sum += game
	}
	fmt.Println(sum)
}
