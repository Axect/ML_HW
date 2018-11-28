extern crate peroxide;
use peroxide::*;

fn main() {
    // Input
    let x = c!(1,3,5);
    let t = c!(4.8,11.3,17.2);

    // 1. Raw Coding
    let xt = x.mul(&t);
    let x2 = x.fmap(|x| x.powf(2.));

    let xm = x.mean();
    let tm = t.mean();
    let xtm = xt.mean();
    let x2m = x2.mean();

    let w1 = (xtm - xm * tm) / (x2m - xm.powf(2.0));
    let w0  = tm - w1 * xm;

    w1.print();
    w0.print();

    // 2. Use Peroxide - Polynomial
    let linreg = least_square(x, t);
    linreg.print();
}
