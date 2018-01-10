package main

import(
	"fmt"
	"strings" //ToUpper TrimSpace
	"bufio" //Reader
	"os"
	"time"
)

//declare function with func
//main will always be auto run
func main(){
	fmt.Println("Hello, I am using GO")
	fmt.Println(strings.ToUpper("yeah!"))

	str1 := "I"
	str2 := "am"
	str3 := "genius"

	//returns an integer string len and err obj
	//must address all of them, if not must use _ to ignore
	strlen, err := fmt.Println(str1, str2, str3)

	if err == nil{
		fmt.Println("Hi")
		fmt.Println("The string length is", strlen)
		//formatted printing
		fmt.Printf("The value of str3 is %v\n",str3)
		fmt.Printf("The type of str3 is %T\n",str3)
		//returns a string and print
		result := fmt.Sprintf("Hello GO")
		fmt.Println("Hi")
		fmt.Println(result)
	}

	//declare a variable
	var s string 
	//for an typed variable, use = instead
	s = "hey"
	fmt.Println(s)
	fmt.Scanln(&s)
	fmt.Println(s)

	//scanning a line
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter text: ")
	s, err = reader.ReadString('\n')

	if err == nil{
		fmt.Println(s)
	}

	//Time obj
	now := time.Now()
	fmt.Printf("The time now is %s\n",now)

}