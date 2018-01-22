package main

import(
	"fmt"
	"os"
	"io"
)

func checkErr(err error){
	if err != nil{
		//interupt the program
		panic(err)
	}
}

func main(){
	//Reading from file without encapsulation
	infile, err := os.Open("data.csv")

	if err == nil{
		fmt.Println(infile)
	} else {
		fmt.Println(err)
	}

	//Writing to file
	outfile, err := os.Create("data.csv")
	checkErr(err)
	defer outfile.Close()

	ln, err := io.WriteString(outfile, "New String")
	checkErr(err)
	fmt.Printf("All done with file of %v characters\n", ln)

	//Reading from file
	infile, err2 := os.Open("data.csv")

	if err2 == nil{
		fmt.Println(infile)
	} else {
		fmt.Println(err)
	}

}