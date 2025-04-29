use std::io;
fn main(){
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Erro ao ler a entrada");
    let mut valores: Vec<i32> = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse().expect("Erro ao converter para inteiro"))
        .collect();

    valores.sort();
    println!("{}", valores[1]);
}
