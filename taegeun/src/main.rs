extern crate peroxide;
use peroxide::*;

fn main() {
    let a = poly(c!(1,3,2));
    let b = poly(c!(1,1));
    a.print();
    b.print();
    let (quot, rem) = a / b;
    quot.print();
    rem.print();
}
