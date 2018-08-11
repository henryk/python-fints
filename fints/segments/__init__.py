import re

from fints.formals import Container, ContainerMeta, SegmentHeader, DataElementGroupField, DataElementField, ReferenceMessage, SegmentSequenceField, SecurityProfile, SecurityIdentificationDetails, SecurityDateTime, EncryptionAlgorithm, KeyName, Certificate, HashAlgorithm, SignatureAlgorithm, UserDefinedSignature, Response, AccountInformation, AccountLimit, AllowedTransaction, ParameterTwostepTAN1, ParameterTwostepTAN3, ParameterPinTan, SupportedLanguages2, SupportedHBCIVersions2, BankIdentifier

from fints.utils import classproperty, SubclassesMixin

TYPE_VERSION_RE = re.compile(r'^([A-Z]+)(\d+)$')

class FinTS3SegmentOLD:
    type = '???'
    country_code = 280
    version = 2
    def __init__(self, segmentno, data):
        self.segmentno = segmentno
        self.data = data
    def __str__(self):
        res = '{}:{}:{}'.format(self.type, self.segmentno, self.version)
        for d in self.data:
            res += '+' + str(d)
        return res + "'"

class FinTS3SegmentMeta(ContainerMeta):
    @staticmethod
    def _check_fields_recursive(instance):
        for name, field in instance._fields.items():
            if not isinstance(field, (DataElementField, DataElementGroupField)):
                raise TypeError("{}={!r} is not DataElementField or DataElementGroupField".format(name, field))
            if isinstance(field, DataElementGroupField):
                FinTS3SegmentMeta._check_fields_recursive(field.type)

    def __new__(cls, name, bases, classdict):
        retval = super().__new__(cls, name, bases, classdict)
        FinTS3SegmentMeta._check_fields_recursive(retval)
        return retval

class FinTS3Segment(Container, SubclassesMixin, metaclass=FinTS3SegmentMeta):
    header = DataElementGroupField(type=SegmentHeader, _d="Segmentkopf")

    @classproperty
    def TYPE(cls):
        match = TYPE_VERSION_RE.match(cls.__name__)
        if match:
            return match.group(1)

    @classproperty
    def VERSION(cls):
        match = TYPE_VERSION_RE.match(cls.__name__)
        if match:
            return int( match.group(2) )

    def __init__(self, *args, **kwargs):
        if 'header' not in kwargs:
            kwargs['header'] = SegmentHeader(self.TYPE, None, self.VERSION)

        args = (kwargs.pop('header'), ) + args

        return super().__init__(*args, **kwargs)

    @classmethod
    def find_subclass(cls, segment):
        h = SegmentHeader.naive_parse(segment[0])
        target_cls = None

        for possible_cls in cls._all_subclasses():
            if getattr(possible_cls, 'TYPE', None) == h.type and getattr(possible_cls, 'VERSION', None) == h.version:
                target_cls = possible_cls

        if not target_cls:
            target_cls = cls

        return target_cls

class HNHBK3(FinTS3Segment):
    message_size = DataElementField(type='dig', length=12)
    hbci_version = DataElementField(type='num', max_length=3)
    dialogue_id = DataElementField(type='id')
    message_number = DataElementField(type='num', max_length=4)
    reference_message = DataElementGroupField(type=ReferenceMessage, required=False)

class HNHBS1(FinTS3Segment):
    message_number = DataElementField(type='num', max_length=4)


class HNVSD1(FinTS3Segment):
    data = SegmentSequenceField()

class HNVSK3(FinTS3Segment):
    security_profile = DataElementGroupField(type=SecurityProfile)
    security_function = DataElementField(type='code', max_length=3)
    security_role = DataElementField(type='code', max_length=3)
    security_identification_details = DataElementGroupField(type=SecurityIdentificationDetails)
    security_datetime = DataElementGroupField(type=SecurityDateTime)
    encryption_algorithm = DataElementGroupField(type=EncryptionAlgorithm)
    key_name = DataElementGroupField(type=KeyName)
    compression_function = DataElementField(type='code', max_length=3)
    certificate = DataElementGroupField(type=Certificate, required=False)

class HNSHK4(FinTS3Segment):
    security_profile = DataElementGroupField(type=SecurityProfile)
    security_function = DataElementField(type='code', max_length=3)
    security_reference = DataElementField(type='an', max_length=14)
    security_application_area = DataElementField(type='code', max_length=3)
    security_role = DataElementField(type='code', max_length=3)
    security_identification_details = DataElementGroupField(type=SecurityIdentificationDetails)
    security_reference_number = DataElementField(type='num', max_length=16)
    security_datetime = DataElementGroupField(type=SecurityDateTime)
    hash_algorithm = DataElementGroupField(type=HashAlgorithm)
    signature_algorithm = DataElementGroupField(type=SignatureAlgorithm)
    key_name = DataElementGroupField(type=KeyName)
    certificate = DataElementGroupField(type=Certificate, required=False)

class HNSHA2(FinTS3Segment):
    security_reference = DataElementField(type='an', max_length=14)
    validation_result = DataElementField(type='bin', max_length=512, required=False)
    user_defined_signature = DataElementGroupField(type=UserDefinedSignature, required=False)

class HIRMG2(FinTS3Segment):
    responses = DataElementGroupField(type=Response, min_count=1, max_count=99)

class HIRMS2(FinTS3Segment):
    responses = DataElementGroupField(type=Response, min_count=1, max_count=99)

class HIUPA4(FinTS3Segment):
    user_identifier = DataElementField(type='id')
    upd_version = DataElementField(type='num', max_length=3)
    upd_usage = DataElementField(type='code', length=1)
    username = DataElementField(type='an', max_length=35, required=False)
    extension = DataElementField(type='an', max_length=2048, required=False)

class HIUPD6(FinTS3Segment):
    account_information = DataElementGroupField(type=AccountInformation, required=False)
    iban = DataElementField(type='an', max_length=34)
    customer_id = DataElementField(type='id')
    account_type = DataElementField(type='num', max_length=2)
    account_currency = DataElementField(type='cur')
    name_account_owner_1 = DataElementField(type='an', max_length=27)
    name_account_owner_2 = DataElementField(type='an', max_length=27, required=False)
    account_product_name = DataElementField(type='an', max_length=30, required=False)
    account_limit = DataElementGroupField(type=AccountLimit, required=False)
    allowed_transactions = DataElementGroupField(type=AllowedTransaction, max_count=999, required=False)
    extension = DataElementField(type='an', max_length=2048, required=False)

class HISYN4(FinTS3Segment):
    customer_system_id = DataElementField(type='id')
    message_number = DataElementField(type='num', max_length=4, required=False)
    security_reference_signature_key = DataElementField(type='num', max_length=16, required=False)
    security_reference_digital_signature = DataElementField(type='num', max_length=16, required=False)

class ParameterSegment(FinTS3Segment):
    max_number_tasks = DataElementField(type='num', max_length=3, _d="Maximale Anzahl Aufträge")
    min_number_signatures = DataElementField(type='num', length=1, _d="Anzahl Signaturen mindestens")
    security_class = DataElementField(type='num', length=1, _d="Sicherheitsklasse")

class HITANS1(ParameterSegment):
    parameters = DataElementGroupField(type=ParameterTwostepTAN1)

class HITANS3(ParameterSegment):
    parameters = DataElementGroupField(type=ParameterTwostepTAN3)

class HIPINS1(ParameterSegment):
    """PIN/TAN-spezifische Informationen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN 
    """
    parameters = DataElementGroupField(type=ParameterPinTan, _d="Parameter PIN/TAN-spezifische Informationen") 


class HIBPA3(FinTS3Segment):
    bpd_version = DataElementField(type='num', max_length=3)
    bank_identifier = DataElementGroupField(type=BankIdentifier)
    bank_name = DataElementField(type='an', max_length=60)
    number_tasks = DataElementField(type='num', max_length=3)
    supported_languages = DataElementGroupField(type=SupportedLanguages2)
    supported_hbci_version = DataElementGroupField(type=SupportedHBCIVersions2)
    max_message_length = DataElementField(type='num', max_length=4, required=False)
    min_timeout = DataElementField(type='num', max_length=4, required=False)
    max_timeout = DataElementField(type='num', max_length=4, required=False)
