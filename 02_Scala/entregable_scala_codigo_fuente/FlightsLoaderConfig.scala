package entregable.FlightsLoader

import com.typesafe.config.{Config, ConfigFactory}

object FlightsLoaderConfig {
  /**
   * This object is used to load the configuration file
   */
  val config: Config = ConfigFactory.load().getConfig("flightsLoader")
  val filePath: String = config.getString("filePath").split(";").head
  val hasHeaders: Boolean = config.getString("filePath").split(";").head.toBoolean
  val headersLength: Int = config.getStringList("headers").size()
  val delimiter: String = config.getString("delimiter").split(";").head
  val outputDir: String = config.getString("outputDir").split(";").head
  val headers: List[String] = config.getStringList("headers").toArray.map(x => x.asInstanceOf[String]).toList
  val columnIndexMap: Map[String, Int] = headers.map(x => (x, headers.indexOf(x))).toMap
  val filteredOrigin: List[String] = config.getStringList("filteredOrigin").toArray.map(x => x.asInstanceOf[String]).toList
}
