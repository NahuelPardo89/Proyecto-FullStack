-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ampa
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ampa
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ampa` DEFAULT CHARACTER SET utf8 ;
USE `ampa` ;

-- -----------------------------------------------------
-- Table `ampa`.`instalaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`instalaciones` (
  `idInstalacion` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`idInstalacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`departamento` (
  `idDepto` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDepto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`users` (
  `idUser` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `Telefono` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `contraseña` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`empleados` (
  `idEmpleado` INT NOT NULL AUTO_INCREMENT,
  `idUser` INT NOT NULL,
  `idDepto` INT NOT NULL,
  `idInstalacion` INT NOT NULL,
  `Horario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEmpleado`),
  INDEX `IdDepartamento_idx` (`idDepto` ASC) VISIBLE,
  INDEX `idInstalacion_idx` (`idInstalacion` ASC) VISIBLE,
  INDEX `idPersonaEmpleados_idx` (`idUser` ASC) VISIBLE,
  CONSTRAINT `IdDepartamentoPersonal`
    FOREIGN KEY (`idDepto`)
    REFERENCES `ampa`.`departamento` (`idDepto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idInstalacionPersonal`
    FOREIGN KEY (`idInstalacion`)
    REFERENCES `ampa`.`instalaciones` (`idInstalacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPersonaEmpleados`
    FOREIGN KEY (`idUser`)
    REFERENCES `ampa`.`users` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`Proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`Proveedores` (
  `idProveedor` INT NOT NULL AUTO_INCREMENT,
  `idEmpleado` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `empresa` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProveedor`),
  INDEX `idEmpleadoProveedor_idx` (`idEmpleado` ASC) VISIBLE,
  CONSTRAINT `idEmpleadoProveedor`
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `ampa`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`productos` (
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
    REFERENCES `ampa`.`Proveedores` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`Clientes` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `idUser` INT NOT NULL,
  `socio` TINYINT NOT NULL,
  PRIMARY KEY (`idCliente`),
  INDEX `idPersonaCliente_idx` (`idUser` ASC) VISIBLE,
  CONSTRAINT `idPersonaCliente`
    FOREIGN KEY (`idUser`)
    REFERENCES `ampa`.`users` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`CarritoProductos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`CarritoProductos` (
  `idCarrito` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idEmpleado` INT NOT NULL,
  PRIMARY KEY (`idCarrito`),
  INDEX `idClientes_idx` (`idCliente` ASC) VISIBLE,
  INDEX `idPersonal_idx` (`idEmpleado` ASC) VISIBLE,
  CONSTRAINT `idClientesCarritoP`
    FOREIGN KEY (`idCliente`)
    REFERENCES `ampa`.`Clientes` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPersonalCarritoP`
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `ampa`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`detalleCarritoProductos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`detalleCarritoProductos` (
  `idDetalle` INT NOT NULL AUTO_INCREMENT,
  `idCarrito` INT NOT NULL,
  `idProducto` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `monto` INT NOT NULL,
  PRIMARY KEY (`idDetalle`),
  INDEX `idCarrito_idx` (`idCarrito` ASC) VISIBLE,
  INDEX `idProd_idx` (`idProducto` ASC) VISIBLE,
  CONSTRAINT `idCarritoDetalle`
    FOREIGN KEY (`idCarrito`)
    REFERENCES `ampa`.`CarritoProductos` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idProdDetalle`
    FOREIGN KEY (`idProducto`)
    REFERENCES `ampa`.`productos` (`idProd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`CarritoReservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`CarritoReservas` (
  `idCarrito` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idEmpleado` INT NOT NULL,
  PRIMARY KEY (`idCarrito`),
  INDEX `idClientes_idx` (`idCliente` ASC) VISIBLE,
  INDEX `idePersonal_idx` (`idEmpleado` ASC) VISIBLE,
  CONSTRAINT `idClienteCarritoR`
    FOREIGN KEY (`idCliente`)
    REFERENCES `ampa`.`Clientes` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPerdonalCarritoR`
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `ampa`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ampa`.`detalleCarritoReservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ampa`.`detalleCarritoReservas` (
  `idDetalle` INT NOT NULL AUTO_INCREMENT,
  `idInstalacion` INT NOT NULL,
  `idCarritoReservas` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `monto` INT NOT NULL,
  PRIMARY KEY (`idDetalle`),
  INDEX `idInstalacion_idx` (`idInstalacion` ASC) VISIBLE,
  INDEX `idCarritoReserva_idx` (`idCarritoReservas` ASC) VISIBLE,
  CONSTRAINT `idInstalacionDetalle`
    FOREIGN KEY (`idInstalacion`)
    REFERENCES `ampa`.`instalaciones` (`idInstalacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idCarritoReservaDetalle`
    FOREIGN KEY (`idCarritoReservas`)
    REFERENCES `ampa`.`CarritoReservas` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
