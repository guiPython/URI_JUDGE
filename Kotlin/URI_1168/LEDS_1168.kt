fun Leds(numero:String): Int {
    val led_algarismo = mutableListOf<Int>(6,2,5,5,4,5,6,3,7,6)
    var numero_leds = 0
    // Diferenca por 48 pois estamos convertendo char em Int o Int de retorno e Unicode
    for (x in numero) numero_leds += led_algarismo[x.toInt() - 48]
    return numero_leds
}
fun main(){
    val qtd_numeros:Int = readLine()!!.toInt()
    for (x in 1..qtd_numeros) {
        val numero: String = readLine()!!.toString()
        println("${Leds(numero)} leds")
    }
}
