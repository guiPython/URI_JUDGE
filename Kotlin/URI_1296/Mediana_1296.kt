import java.io.EOFException
import java.lang.NumberFormatException
import kotlin.math.sqrt

fun Triangulo(lista:List<Float>){
    lista.sorted()
    if (lista[0] + lista[1] > lista[2]){
        println(lista[0])
        //Formula de Heron
        val s_perimetro = (lista.sum())/2.00
        val area = sqrt((s_perimetro*(s_perimetro-lista[0])*(s_perimetro-lista[1])*(s_perimetro-lista[2])))
        println("%.3f".format(4*area/3))
    }
    else{
        println("-1.000")
    }
}


fun main(){
    while (true) {
        try{
            val (a,b,c)= readLine()!!.split(' ').map(String::toFloat)
            val medianas = listOf<Float>(a,b,c)
            print(medianas)
            Triangulo(medianas)
        }
        catch (e: NumberFormatException){
            break
        }
        catch (e : EOFException){
            break
        }
    }
}