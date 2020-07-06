fun main(arg:Array<String>){
    val nome = readLine()!!.toString()
    val salario = readLine()!!.toFloat()  ; val montante = readLine()!!.toFloat()
    println("TOTAL = R$${"%.2f".format(salario+0.15*montante)}")
}