import kotlin.math.pow
fun Vol_Esfera(r:Double):Double = (4/3.0) * 3.14159 * r.pow(3)
fun main(arg:Array<String>){
    val raio:Double = readLine()!!.toDouble()
    println("VOLUME = %.3f".format(Vol_Esfera((raio))))
}

