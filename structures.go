package main

import (
	"fmt"
)

func main() {

	//declaring slice and array
	slice1 := []string{"hello", "how", "when"}
	var array2 = [3]int{1,2,3}


	/* not working examples
	var slice2 [3]int = {1,2,3}

	var slice3 //here expecting type
	slice3 = [3]int{1,2,3}
	*/

	//this works
	var slice3 []int
	slice3 = []int{1,2,3}
	//this doesn't
	//slice3 = {1,2,3}

	//modify by index
	slice3[0]=5

	//modify slice by func
	//append(slice1,"who")// evaluated but not used not the same idea as non-type in python
	slice1 = append(slice1, "who")
	fmt.Println(slice1, array2, slice3)

	//append func can do slicing then append
	slice1 = append(slice1[1:],"whose")
	slice1 = slice1[1:]
	fmt.Println(slice1)

	//using make to declare with initial size and cap
	//then can use index to access
	numbers1 := make([]int, 5)
	//new will not initialize memory and returns a pointer
	numbers2 := new([]int)
	fmt.Println(numbers1, *numbers2)

	//when declare map using make
	map1 := make(map[string]int)
	map1["hello"] = 1
	fmt.Println(map1)
}
