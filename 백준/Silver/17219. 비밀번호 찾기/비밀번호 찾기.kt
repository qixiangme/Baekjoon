
import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    BufferedReader(InputStreamReader(System.`in`)).use { r ->
        val (n, m) = r.readLine().split(" ").map { it.toInt() }
        val answer = StringBuilder()
        val map = mutableMapOf<String, String>()
        
        repeat(n) {
            val (site, password) = r.readLine().split(" ")
            map[site] = password
        }
        
        repeat(m) {
            answer.appendLine(map[r.readLine()])
        }
        
        println(answer);
    }
}