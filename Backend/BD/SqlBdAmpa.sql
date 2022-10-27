-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ampav1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ampav1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ampav1` DEFAULT CHARACTER SET utf8 ;
USE `ampav1` ;

-- -----------------------------------------------------
-- Table `ampav1`.`instalaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`instalaciones` (
  `idInstalacion` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `precio` INT NOT NULL,
  PRIMARY KEY (`idInstalacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`users` (
  `idUser` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `Telefono` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `contraseña` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`empleados` (
  `idEmpleado` INT NOT NULL AUTO_INCREMENT,
  `idUser` INT NOT NULL,
  `idInstalacion` INT NOT NULL,
  `Horario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEmpleado`, `idUser`),
  INDEX `idInstalacion_idx` (`idInstalacion` ASC) VISIBLE,
  INDEX `idPersonaEmpleados_idx` (`idUser` ASC) VISIBLE,
  CONSTRAINT `idInstalacionPersonal`
    FOREIGN KEY (`idInstalacion`)
    REFERENCES `ampav1`.`instalaciones` (`idInstalacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPersonaEmpleados`
    FOREIGN KEY (`idUser`)
    REFERENCES `ampav1`.`users` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`Proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`Proveedores` (
  `idProveedor` INT NOT NULL AUTO_INCREMENT,
  `idEmpleado` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `empresa` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProveedor`),
  INDEX `idEmpleadoProveedor_idx` (`idEmpleado` ASC) VISIBLE,
  CONSTRAINT `idEmpleadoProveedor`
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `ampav1`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`productos` (
  `idProd` INT NOT NULL AUTO_INCREMENT,
  `idProveedor` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `marca` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `precio` INT NOT NULL,
  `stock` INT NOT NULL,
  `foto` VARCHAR(5000) NOT NULL,
  PRIMARY KEY (`idProd`),
  INDEX `Idproveedor_idx` (`idProveedor` ASC) VISIBLE,
  CONSTRAINT `IdproveedorProd`
    FOREIGN KEY (`idProveedor`)
    REFERENCES `ampav1`.`Proveedores` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`Clientes` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `idUser` INT NOT NULL,
  `socio` TINYINT NOT NULL,
  PRIMARY KEY (`idCliente`, `idUser`),
  INDEX `idPersonaCliente_idx` (`idUser` ASC) VISIBLE,
  CONSTRAINT `idPersonaCliente`
    FOREIGN KEY (`idUser`)
    REFERENCES `ampav1`.`users` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`CarritoProductos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`CarritoProductos` (
  `idCarrito` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idEmpleado` INT NOT NULL,
  `monto` INT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`idCarrito`),
  INDEX `idClientes_idx` (`idCliente` ASC) VISIBLE,
  INDEX `idPersonal_idx` (`idEmpleado` ASC) VISIBLE,
  CONSTRAINT `idClientesCarritoP`
    FOREIGN KEY (`idCliente`)
    REFERENCES `ampav1`.`Clientes` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPersonalCarritoP`
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `ampav1`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`detalleCarritoProductos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`detalleCarritoProductos` (
  `idDetalleProducto` INT NOT NULL AUTO_INCREMENT,
  `idCarritoProductos` INT NOT NULL,
  `idProducto` INT NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`idDetalleProducto`, `idCarritoProductos`),
  INDEX `idCarrito_idx` (`idCarritoProductos` ASC) VISIBLE,
  INDEX `idProd_idx` (`idProducto` ASC) VISIBLE,
  CONSTRAINT `idCarritoDetalle`
    FOREIGN KEY (`idCarritoProductos`)
    REFERENCES `ampav1`.`CarritoProductos` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idProdDetalle`
    FOREIGN KEY (`idProducto`)
    REFERENCES `ampav1`.`productos` (`idProd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`CarritoReservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`CarritoReservas` (
  `idCarrito` INT NOT NULL AUTO_INCREMENT,
  `idEmpleado` INT NOT NULL,
  `idCliente` INT NOT NULL,
  `monto` INT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`idCarrito`),
  INDEX `idClientes_idx` (`idCliente` ASC) VISIBLE,
  INDEX `idePersonal_idx` (`idEmpleado` ASC) VISIBLE,
  CONSTRAINT `idClienteCarritoR`
    FOREIGN KEY (`idCliente`)
    REFERENCES `ampav1`.`Clientes` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPerdonalCarritoR`
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `ampav1`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampav1`.`detalleCarritoReservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampav1`.`detalleCarritoReservas` (
  `idDetalleReserva` INT NOT NULL AUTO_INCREMENT,
  `idCarritoReservas` INT NOT NULL,
  `idInstalacion` INT NOT NULL,
  PRIMARY KEY (`idDetalleReserva`, `idCarritoReservas`),
  INDEX `idInstalacion_idx` (`idInstalacion` ASC) VISIBLE,
  INDEX `idCarritoReserva_idx` (`idCarritoReservas` ASC) VISIBLE,
  CONSTRAINT `idInstalacionDetalle`
    FOREIGN KEY (`idInstalacion`)
    REFERENCES `ampav1`.`instalaciones` (`idInstalacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idCarritoReservaDetalle`
    FOREIGN KEY (`idCarritoReservas`)
    REFERENCES `ampav1`.`CarritoReservas` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
