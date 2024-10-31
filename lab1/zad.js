let lista = [
    [12,400],
    [1,3],
    [75,90],
    [14,96]
]
let plecak = 40;
let zero = 0;
let cena = 0;
const algPlecaka = (list,maxWaga) => {
        list.sort((a,b) => b[1] - a[1]);
        for(let i = 0; i < list.length; i++){
            if((list[i][0] + zero) <= maxWaga){
                zero += list[i][0]
                cena += list[i][1]
            }
        }
        console.log('Sortowane elementy')
        console.log(list)
}
algPlecaka(lista, plecak)
console.log('Waga w plecaku: '+ zero);
console.log('MaxWaga w plecaku: '+ plecak);
console.log('Cena items w plecaku: '+ cena);

