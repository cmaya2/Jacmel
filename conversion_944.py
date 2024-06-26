import xml.etree.ElementTree as et
from datetime import datetime
import psycopg2
import os
import sys

# Database settings
connection = psycopg2.connect(
    host='localhost',
    database='sequencer',
    user='Admin',
    password='@Dm1n'
)


class Convert_944:

    def __init__(self, XML, path, mantis_import_path, transaction_number, client_id, connection):
        self.XML = XML
        self.path = path
        self.mantis_import_path = mantis_import_path
        self.transaction_number = transaction_number
        self.client_id = client_id
        self.connection = connection

    def parse_xml(self):
        # Load in the edi file based on function that checks directory of file out of Class structure
        formatfilename = str(self.XML)
        remove_extension = formatfilename.split(".")
        rem_extension = remove_extension[0].split("\\")
        oak = et.parse(self.XML)
        rooted = oak.getroot()
        counter = 0
        segment_count = 0
        for element in rooted.iter():
            if element.tag == 'ReceiptHeader':
                for ReceiptHeader_child_element in element:
                    if ReceiptHeader_child_element.tag == 'ReceiptNumber':
                        receipt_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'DepositorOrderNumber':
                        depositor_order_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'ShipmentID':
                        shipment_id = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'PurchaseOrderNumber':
                        purchase_order_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalQuantityShipped':
                        total_quantity_shipped = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalShipmentWeight':
                        total_shipment_weight = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'PackWeightUnitOfMeasure':
                        header_pack_weight_unit_of_measure = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalShipmentVolume':
                        total_shipment_volume = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'VolumeUnitOfMeasure':
                        volume_unit_of_measure = ReceiptHeader_child_element.text
            if element.tag == 'ShipTo':
                for ShipTo_child_element in element:
                    if ShipTo_child_element.tag == 'Name':
                        ship_to_name = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Code':
                        ship_to_code = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Address1':
                        ship_to_address1 = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Address2':
                        ship_to_address2 = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'City':
                        ship_to_city = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'State':
                        ship_to_state = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ZipCode':
                        ship_to_zipcode = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Country':
                        ship_to_country = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactName':
                        ship_to_contact_name = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactPhone':
                        ship_to_contact_phone = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactEmail':
                        ship_to_contact_email = ShipTo_child_element.text
            if element.tag == 'ShipFrom':
                for ShipFrom_child_element in element:
                    if ShipFrom_child_element.tag == 'Name':
                        ship_from_name = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'Code':
                        ship_from_code = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'Address1':
                        ship_from_address1 = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'Address2':
                        ship_from_address2 = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'City':
                        ship_from_city = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'State':
                        ship_fromo_state = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'ZipCode':
                        ship_from_zipcode = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'Country':
                        ship_from_country = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'ContactName':
                        ship_from_contact_name = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'ContactPhone':
                        ship_from_contact_phone = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'ContactEmail':
                        ship_from_contact_email = ShipFrom_child_element.text
            if element.tag == 'Dates':
                for Dates_child_element in element:
                    if Dates_child_element.tag == 'PurchaseOrderDate':
                        purchase_order_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'ShipDate':
                        ship_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'EstimatedDeliveryDate':
                        estimated_delivery_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'ScheduledDeliveryDate':
                        scheduled_delivery_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'PickupDate':
                        pick_up_date = Dates_child_element.text
            if element.tag == 'ReferenceInformation':
                for ReferenceInformation_child_element in element:
                    if ReferenceInformation_child_element.tag == 'BillOfLadingNumber':
                        bill_of_lading_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'ContainerNumber':
                        waybill_holding = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'SealNumber':
                        seal_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'ReferenceNumber':
                        reference_number = ReferenceInformation_child_element.text
        # try:
        #     if len(shipment_id) > 0:
        #         pass
        # except TypeError:
        #     os.replace(self.XML, self.path + "In\\Archive\\" + self.transaction_number + "\\shipid_" + rem_extension[8] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt")
        #     raise Exception("This reciept confirmation processed without a shipment ID")
        cursor = connection.cursor()
        cursor.execute("SELECT sequence_number FROM public.sequence where client='general'")
        data = cursor.fetchone()
        sequence_number = int(data[0]) + 1
        cursor.execute("update sequence set sequence_number =" + str(sequence_number) + " where client='general'")
        connection.commit()
        header_string = 'ISA*00*          *00*          *ZZ*GPALOGISTICS   *12*7183494307     *' + datetime.now().strftime("%y%m%d") + '*' + datetime.now().strftime("%H%M") + '*U*00403*' + str(sequence_number) + '*0*P*>~' \
                        'GS*RE*GPALOGISTICS*7183494307*' + datetime.now().strftime("%Y%m%d") + '*' + datetime.now().strftime("%H%M") + '*' + str(sequence_number)[-4:] + '*X*004030~' \
                        'ST*944*1001~' \
                        'W17*F*' + datetime.now().strftime("%Y%m%d") + '*' + depositor_order_number + '*' + purchase_order_number + '*' + shipment_id + '~' \
                        'N1*WH*GPA Logistics Group~' \
                        'N9*PO*' + str(purchase_order_number) + '~' \
                        'G62*09*' + datetime.now().strftime("%Y%m%d") + '~'
        for element in rooted.iter():
            if element.tag == 'ReceiptDetail':
                for ReceiptDetail_child_element in element:
                    item_upc = ''
                    if ReceiptDetail_child_element.tag == 'Item':
                        counter = counter + 1
                        item_upc = ""
                        for Item_sub_element in ReceiptDetail_child_element:
                            if Item_sub_element.tag == 'ItemNumber':
                                item_number = Item_sub_element.text
                            elif Item_sub_element.tag == 'ItemUPC':
                                item_upc = Item_sub_element.text
                            elif Item_sub_element.tag == 'CaseUPC':
                                case_upc = Item_sub_element.text
                            elif Item_sub_element.tag == 'GTIN':
                                gtin = Item_sub_element.text
                            elif Item_sub_element.tag == 'ReceivedQuantity':
                                received_quantity = Item_sub_element.text
                            elif Item_sub_element.tag == 'ShippedQuantity':
                                shipped_quantity = Item_sub_element.text
                            elif Item_sub_element.tag == 'QuantityUnitOfMeasure':
                                quantity_unit_of_measure = Item_sub_element.text
                            elif Item_sub_element.tag == 'ItemDescription':
                               item_description = Item_sub_element.text
                            elif Item_sub_element.tag == 'ProductGroup':
                                product_group = Item_sub_element.text
                            elif Item_sub_element.tag == 'AlternateItemNumber':
                                alternate_item_number = Item_sub_element.text
                            elif Item_sub_element.tag == 'LotNumber':
                                lot_number = 'WC'
                            elif Item_sub_element.tag == 'SKU':
                                sku = Item_sub_element.text
                            elif Item_sub_element.tag == 'Style':
                                style = Item_sub_element.text
                            elif Item_sub_element.tag == 'Color':
                                color = Item_sub_element.text
                            elif Item_sub_element.tag == 'Size':
                                size = Item_sub_element.text
                            elif Item_sub_element.tag == 'LabelCode':
                                label_code = Item_sub_element.text
                            elif Item_sub_element.tag == 'ProductType':
                                product_type = Item_sub_element.text
                            elif Item_sub_element.tag == 'ItemLength':
                                item_length = Item_sub_element.text
                            elif Item_sub_element.tag == 'ItemWidth':
                                item_width = Item_sub_element.text
                            elif Item_sub_element.tag == 'ItemHeight':
                                item_height = Item_sub_element.text
                            elif Item_sub_element.tag == 'PackQuantity':
                                pack_quantity = Item_sub_element.text
                            elif Item_sub_element.tag == 'InnerPackQuantity':
                                inner_pack_quantity = '1'
                            elif Item_sub_element.tag == 'PackSize':
                                pack_size = Item_sub_element.text
                            elif Item_sub_element.tag == 'PackSizeUnitOfMeasure':
                                pack_size_unit_of_measure = Item_sub_element.text
                            elif Item_sub_element.tag == 'PackWeight':
                                pack_weight = Item_sub_element.text
                            elif Item_sub_element.tag == 'PackWeightUnitOfMeasure':
                                detail_pack_weight_unit_of_measure = Item_sub_element.text
                            elif Item_sub_element.tag == 'PurchaseOrderNumber':
                                detail_purchase_order_number = Item_sub_element.text
                            elif Item_sub_element.tag == 'OrderLineNumber':
                                order_line_number = Item_sub_element.text
                            elif Item_sub_element.tag == 'Receipt_Color':
                                receipt_color = Item_sub_element.text
                            elif Item_sub_element.tag == 'Receipt_Size':
                                receipt_size = Item_sub_element.text
                            elif Item_sub_element.tag == 'PackVolume':
                                pack_volume = Item_sub_element.text
                            elif Item_sub_element.tag == 'PackVolumeUnitOfMeasure':
                                pack_volume_unit_of_measure = Item_sub_element.text
                        # Generating dynamic values
                        if int(received_quantity) == 0:
                            raise Exception("Container received with a quantity of 0.")
                        body_string = 'LX*' + str(counter) + '~' \
                                      'W07*' + received_quantity + '*EA**VN*' + item_number + '~'
                        header_string = header_string + body_string
                        segment_count = segment_count + 2
        segment_count = segment_count + 7
        print(segment_count)
        footer_string = 'W14*' + received_quantity + '*' + str(total_quantity_shipped) + '~' \
                        'SE*' + str(segment_count) + '*1001~' \
                        'GE*1*' + str(sequence_number)[-4:] + '~' \
                        'IEA*1*' + str(sequence_number) + '~'
        completed_string = header_string + footer_string
        with open(self.path + "Out\\" + self.transaction_number + "_" + self.client_id + "_" + str(depositor_order_number)
                  + "_" + datetime.now().strftime("%Y%m%d%H%M%S" + ".txt"), "w") as acknowledgement_file:
            acknowledgement_file.write(completed_string)
        with open(self.path + "Out\\Archive\\" + self.transaction_number + "\\" + self.transaction_number + "_" +
                  self.client_id + "_" + str(depositor_order_number) + "_" + datetime.now().strftime("%Y%m%d%H%M%S" + ".txt"),
                  "w") as acknowledgement_file:
            acknowledgement_file.write(completed_string)