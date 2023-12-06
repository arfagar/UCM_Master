import sbtassembly.AssemblyPlugin.defaultShellScript

ThisBuild / version := "0.1.0-SNAPSHOT"
ThisBuild / scalaVersion := "2.13.12"
ThisBuild / assemblyPrependShellScript := Some(defaultShellScript)


val mainClassName = "entregable.FlightsLoader.FlightsLoader"


lazy val root = (project in file("."))
  .settings(
    name := "entregable_scala_codigo_fuente", // TODO: establece el nombre del proyecto. Tiene que ser el mismo que el nombre que le has dado al proyecto en IntelliJ
    Compile / run / mainClass:= Some(mainClassName), // TODO: define la clase principal del proyecto para la etapa `run` de `Compile`
    Compile / packageBin/ mainClass:=Some(mainClassName),// TODO: define la clase principal del proyecto para la etapa `packageBin` de `Compile`
    assembly / mainClass:= Some(mainClassName),// TODO: define la clase principal del proyecto para el ensamblado de `assembly`
    assembly / assemblyJarName:= "entregable_scala_codigo_fuente.jar", // TODO: define `flights_loader.jar` como el nombre del jar que se genera en la etapa assembly
    libraryDependencies ++= Seq(
      // TODO añade la dependencia de la librería de configuración de Typesafe

      "org.scalatest" %% "scalatest" % "3.2.17" % Test,
      "org.scala-lang" %% "toolkit-test" % "0.1.7" % Test,
      "com.typesafe" % "config" % "1.4.3",


    )
  )
