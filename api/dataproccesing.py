import pandas as pd
import csv

peopleType = ""
birthday = ""

act = ["GOBIERNO", "TEXTIL", "SERVICIOS PROFESIONALES", "ROPA REGALOS Y CALZADO", "SUPER Y ABARROTES", "ALQUILER DE INMUEBLES", "MAQUIRIA Y EQUIPO", "VIVIENDA", "NO VIVIENDA", "QUIMICO", "TRANSPORTE", "OTROS COMERCIANTES", "HOTELES", "PRODUCTOS A BASE DE MINERALES NO METALICOS", "AGROINDUSTRIA", "SERVICIOS FINANCIEROS",
       "AUTOS Y REFACCIONES", "SERVICIOS DE EDUCACION", "ESTACIONES DE GASOLI Y GASERAS", "INDUSTRIAS BASICAS", "OTRAS INDUSTRIAS MANUFACTURERAS", "SERVICIOS DE ESPARCIMIENTO", "SERVICIOS MEDICOS", "INSUMOS PARA LA INDUSTRIA", "RESTAURANT", "OTROS SERVICIOS", "ELECTRICIDAD", "PAPEL", "MINERIA", "COMUNICACIONES", "?"]  # el 30 no

micro = None

ventas = ["A. Menor a 01M", "B. 01M-02M", "C. 02M-03M", "D. 03M-04M", "E. 04M-05M", "F. 05M-06M", "G. 06M-08M", "H. 08M-10M",
          "I. 10M-12M", "J. 12M-15M", "K. 15M-16M", "L. 16M-18M", "M. 18M-20M", "N. 20M-30M", "O. 30M-40M", "P. 40M-50M", "Q. +50M"]

if __name__ == "__main__":
    

    file = 'dataset.xlsx'
    df = pd.read_excel(file)
    op = []

    for i in df.iterrows():
        if i[1].Tipo_Persona == "Gobierno":
            peopleType = 1
        if i[1].Tipo_Persona == "Morales":
            peopleType = 2
        if i[1].Tipo_Persona == "Físicas":
            peopleType = 3
        if i[1].Tipo_Persona == "PFAEs":
            peopleType = 4
        if i[1].Tipo_Persona == "?":
            peopleType = -1

        if i[1].NB_SEG_NRB_19 == "MICRONEGOCIO BAJO":
            micro = 1

        if i[1].NB_SEG_NRB_19 == "MICRONEGOCIO":
            micro = 2

        row = [
            peopleType,
            # i[1].Sexo,
            i[1].CD_POSTAL,
            i[1].FH_NACIMIENTO,
            act.index(i[1].NB_ACTIVIDAD),
            micro,
            ventas.index(i[1].Rango_Ventas),
            i[1].anitgue,
            i[1].VENTAS_POR_TPV,
            i[1].OFERTA_CREDITO_EN_2018,
            i[1].FH_FORMA_CREDITO_2018,
            i[1].TDCN,
            i[1].DisponibleTarjeta,
            i[1].Bcom,
            i[1].Bneg,
            i[1].Email,
            i[1].C2018,
            i[1].MoraTarj,
            i[1].MoraCS,
            i[1].Saldo,
            i[1].cien,
            i[1].trecientos,
            i[1].seicientos,
            i[1].millon
        ]

        with open('dataset.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()


        # print(row)


    # for j in df:
    #     for i in df[j]:
    #         print(i)
