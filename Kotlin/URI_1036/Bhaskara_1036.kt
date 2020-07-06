
fun Bhaskara(A:Double,B:Double,C:Double){
    val delta = Math.pow(B,2.0) -4*A*C
    if (A == 0.0 || delta < 0.0 )  {println("Impossivel calcular")}
    else{
        val r_delta = Math.pow(delta,0.5)
        val r1 = (-B + r_delta) / (2.0*A)
        val r2 = (-B - r_delta) / (2.0*A)
        println("R1 = ${r1}")
        println("R2 = ${r2}")
    }
}

fun main(){
    val(A,B,C)= readLine()!!.split(" ").map(String::toDouble)
    Bhaskara(A,B,C)
}