package entregable.FlightsLoader

import java.io.File
import scala.io.Source

object FileUtils {

  def isInvalid(s: String): Boolean = {
    /**
     * This function is used to check if the line is valid or not
     *
     * @param s : String
     * @return Boolean: true if the line is invalid, false otherwise
     */
    // TODO: Implementar esta función
    //  asegúrate de que el número de campos es el correcto, `s` representa una línea del csv, para ser inválido:
    //    - debe ser vacío,
    //    - tras hacer un split por el delimitador (ver FlightsLoaderConfig) el número de campos debe ser distinto al
    //      número de headers (ver FlightsLoaderConfig)
    ???
  }

  def loadFile(filePath: String): Seq[Flight] = {
    /**
     * This function is used to load the file
     *
     * @param filePath : String
     * @return Seq[Flight]
     */

    val source = Source.fromFile(new File(filePath))
    val linesList: List[String] = try source.getLines.toList finally source.close()
    val headers = (linesList.head).split(";").toList

    require(headers.size == FlightsLoaderConfig.headersLength, "Number of items in headers does not match the expected amount") // TODO: Comprueba que el número de headers es el correcto comparándolo con headersLength
    //  (ver FlightsLoaderConfig)

    val rows = ??? // TODO: Obtén las filas del fichero csv (sin los headers)
    //  Pista: existen funciones de la clase List que te pueden ayudar

    val invalidRows: List[String] = ??? // TODO: Obtén las filas inválidas.
    //  Pista: usa la función isInvalid para filtrar
    val validRows: List[String] = ??? // TODO: Obtén las filas válidas.
    //  Pista: usa la función isInvalid para filtrar
    val flights: Seq[Flight] = ??? // TODO: Convierte las filas válidas en objetos de tipo Flight y devuélvelos en una lista
    //  Pista: usa la función fromString de Flight
    flights
  }

}
