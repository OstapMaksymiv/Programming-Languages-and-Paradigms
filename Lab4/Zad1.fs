(* For more information see https://aka.ms/fsharp-console-apps
printfn "Hello from F#"

let x : int = 10

printfn "wartosc zmiennej x = %d" x 

let mutable y: int = 20

printfn "wartość y = %d" y

y <- 30

printfn "wartość y po zmianie = %d" y

printf "podaje liczbe: "

let a : int = System.Console.ReadLine() |>int

printfn "podana wartosc a = %d" a


if a >= 18 then
    printfn "Osoba pelnoletnia"
else 
    printfn "Osoba niepelnoletnia"
// instrukcja if then else
// + - *  / % a=0 
let day : int = 3
let dayName: string =
    match day with
    | 1 -> "Poniedziałek"
    | 2 -> "Wtorek"
    | 3 -> "Sroda"
    | 4 -> "Czwartek"
    | 5 -> "Piatek"
    | 6 -> "Sobota"
    | 7 -> "Niedziela"
    | _ -> "Niepoprawny dzien"

printfn "Dzien Tygodnia %s" dayName



let month : int = 1
let MonthName: string =
    match month with
    | 12 | 1 | 2 -> "Zima"
    | 3 | 4 | 5 -> "Wiosna"
    | 6 | 7 | 8 -> "Lato"
    | 9| 10 | 11 -> "Jesien"
    | _ -> "Niepoprawny miesiac"


let listA = []
let listINT = [1;2;3;4;5]
let listINTA = [1..5]

let listaB = [0..2..10] // 0 2 4 6 8 10

let listaC = List.init 5(fun x-> x* x)

let first = List.head listINT
let tail = List.tail listINT
let secend = List.item 2 listINT

let listC = listA @ listaB

List.filter (fun x -> x%2=0)

let arr =[|1;2;3|]
arr.[0] <- 34


type Person ={
    Name:string
    Age:int
}
let person ={Name="Janda"; Age = 12}

let sumaIter n =
    let mutable sum = 0
    for i in 1..n do
        sum <- sum + i
    sum

printfn "Suma iteracyjna %d"

let rec silnia n =
    if n = 0 then 1
    else n* silnia(n-1)

printfn "Silnia %d" (silnia 5)

let silniaOgonow n =
    let rec loop acc n =
        if n = 0 then acc
        else loop (acc *n) (n - 1)
    loop 1 n *)


type User = {Weight: float; Height: float}

//Obliczenie BMI
//Waga(kg)^2/wzrost(m)

let calculateBMI user =
    let heightmetres = user.Height/100.0
    user.Weight / (heightmetres ** 2.0)


let categoryBMI bmi=
    if bmi <18.5 then "Niedowaga"
    elif bmi <24.9 then "Waga Prawidłowa"
    elif bmi <29.9 then "Nadwaga"
    else "Otylosc"


let rec readFloat prompt =
    printfn "%s" prompt
    match System.Double.TryParse(System.Console.ReadLine()) with
    | (true, value) -> value
    |_ -> 
        printfn "Bledne dane. Uzyj popranych danych typu numerycznego"
        readFloat prompt


let main() =
    let weight  = readFloat "Podaj swoja wage w kg: "
    let height = readFloat "Podaj swoj wzrost w cm "


    let user = { Weight = weight; Height = height}

    let bmi = calculateBMI user

    printfn "Twoje BMI wynosi: %.2f" bmi
    printfn "Twoja kategoria BMU %s" (categoryBMI bmi)

main()