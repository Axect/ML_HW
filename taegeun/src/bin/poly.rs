extern crate peroxide;
use peroxide::*;

fn main() {
    let a = poly(c!(1,2,3));
    let b = poly(c!(1,1));
    let (quot, rem) = a / b;
    quot.print();
    rem.print();
}
