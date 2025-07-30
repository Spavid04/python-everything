# This is a generated file, created by generate_headers.py
# Changes made here will be lost when re-running that script
# Input Everything3.h SHA256: 5ccadde782b3a4ddd6429a0439d6b3da1ba722fa148d7d04ecc07831cd4706dd

import enum
import typing


#region Status
class Status(enum.IntEnum):
    OK = 0
    OUT_OF_MEMORY = 0xE0000001
    IPC_PIPE_NOT_FOUND = 0xE0000002
    DISCONNECTED = 0xE0000003
    INVALID_PARAMETER = 0xE0000004
    BAD_REQUEST = 0xE0000005
    CANCELLED = 0xE0000006
    PROPERTY_NOT_FOUND = 0xE0000007
    SERVER = 0xE0000008
    INVALID_COMMAND = 0xE0000009
    BAD_RESPONSE = 0xE000000A
    INSUFFICIENT_BUFFER = 0xE000000B
    SHUTDOWN = 0xE000000C
    INVALID_PROPERTY_VALUE_TYPE = 0xE000000D

StatusToMessageMap = {
    Status.OK: "no error",
    Status.OUT_OF_MEMORY: "out of memory.",
    Status.IPC_PIPE_NOT_FOUND: "IPC pipe server not found (Everything search client is not running)",
    Status.DISCONNECTED: "disconnected from pipe server",
    Status.INVALID_PARAMETER: "invalid parameter",
    Status.BAD_REQUEST: "bad request",
    Status.CANCELLED: "user cancelled",
    Status.PROPERTY_NOT_FOUND: "property not found",
    Status.SERVER: "server error (server out of memory)",
    Status.INVALID_COMMAND: "invalid command",
    Status.BAD_RESPONSE: "bad server response",
    Status.INSUFFICIENT_BUFFER: "not enough room to store response data",
    Status.SHUTDOWN: "shutdown initiated by user",
    Status.INVALID_PROPERTY_VALUE_TYPE: "property value type is incorrect.",
}

def StatusToMessage(status: Status) -> str:
    return StatusToMessageMap.get(status, "<unknown error>")

#region Exceptions
class Everything3Exception(Exception):
    def __init__(self, *args, status: Status):
        super().__init__(*args)
        self.status = status

class E3OutOfMemoryError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.OUT_OF_MEMORY)
class E3IpcPipeNotFoundError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.IPC_PIPE_NOT_FOUND)
class E3DisconnectedError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.DISCONNECTED)
class E3InvalidParameterError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.INVALID_PARAMETER)
class E3BadRequestError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.BAD_REQUEST)
class E3CancelledError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.CANCELLED)
class E3PropertyNotFoundError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.PROPERTY_NOT_FOUND)
class E3ServerError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.SERVER)
class E3InvalidCommandError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.INVALID_COMMAND)
class E3BadResponseError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.BAD_RESPONSE)
class E3InsufficientBufferError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.INSUFFICIENT_BUFFER)
class E3ShutdownError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.SHUTDOWN)
class E3InvalidPropertyValueTypeError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.INVALID_PROPERTY_VALUE_TYPE)

StatusToExceptionTypeMap = {
    Status.OUT_OF_MEMORY: E3OutOfMemoryError,
    Status.IPC_PIPE_NOT_FOUND: E3IpcPipeNotFoundError,
    Status.DISCONNECTED: E3DisconnectedError,
    Status.INVALID_PARAMETER: E3InvalidParameterError,
    Status.BAD_REQUEST: E3BadRequestError,
    Status.CANCELLED: E3CancelledError,
    Status.PROPERTY_NOT_FOUND: E3PropertyNotFoundError,
    Status.SERVER: E3ServerError,
    Status.INVALID_COMMAND: E3InvalidCommandError,
    Status.BAD_RESPONSE: E3BadResponseError,
    Status.INSUFFICIENT_BUFFER: E3InsufficientBufferError,
    Status.SHUTDOWN: E3ShutdownError,
    Status.INVALID_PROPERTY_VALUE_TYPE: E3InvalidPropertyValueTypeError,
}

def StatusToExceptionType(status: Status) -> typing.Optional[typing.Type[Everything3Exception]]:
    return StatusToExceptionTypeMap.get(status, None)
#endregion
#endregion

#region Target Machine
class TargetMachine(enum.IntEnum):
    UNKNOWN = 0
    X86 = 1
    X64 = 2
    ARM = 3
    ARM64 = 4
#endregion

#region Folder First Option
class FolderFirst(enum.IntEnum):
    ASCENDING = 0
    ALWAYS = 1
    NEVER = 2
    DESCENDING = 3
#endregion

#region Property Type
class PropertyType(enum.IntEnum):
    NONE = 0
    METADATA = 1
    FILE = 2
    INDEX = 3
    CONTENT = 4
    VOLUME = 5
    SEARCH = 6
    PROPERTY_SYSTEM = 7
#endregion

#region Property Value
class PropertyValueType(enum.IntEnum):
    NULL = 0
    BYTE = 1
    WORD = 2
    DWORD = 3
    DWORD_FIXED_Q1K = 4
    UINT64 = 5
    UINT128 = 6
    DIMENSIONS = 7
    PSTRING = 8
    PSTRING_MULTISTRING = 9
    PSTRING_STRING_REFERENCE = 10
    SIZE_T = 11
    INT32_FIXED_Q1K = 12
    INT32_FIXED_Q1M = 13
    PSTRING_FOLDER_REFERENCE = 14
    PSTRING_FILE_OR_FOLDER_REFERENCE = 15
    BLOB8 = 16
    DWORD_GET_TEXT = 17
    WORD_GET_TEXT = 18
    BLOB16 = 19
    BYTE_GET_TEXT = 20
    PROPVARIANT = 21
#endregion

#region Property ID
class PropertyId(enum.IntEnum):
    INVALID_PROPERTY_ID = 0xffffffff
    NAME = 0
    PATH = 1
    SIZE = 2
    EXTENSION = 3
    TYPE = 4
    DATE_MODIFIED = 5
    DATE_CREATED = 6
    DATE_ACCESSED = 7
    ATTRIBUTES = 8
    DATE_RECENTLY_CHANGED = 9
    RUN_COUNT = 10
    DATE_RUN = 11
    FILE_LIST_FILENAME = 12
    WIDTH = 13
    HEIGHT = 14
    DIMENSIONS = 15
    ASPECT_RATIO = 16
    BIT_DEPTH = 17
    LENGTH = 18
    AUDIO_SAMPLE_RATE = 19
    AUDIO_CHANNELS = 20
    AUDIO_BITS_PER_SAMPLE = 21
    AUDIO_BIT_RATE = 22
    AUDIO_FORMAT = 23
    FILE_SIGNATURE = 24
    TITLE = 25
    ARTIST = 26
    ALBUM = 27
    YEAR = 28
    COMMENT = 29
    TRACK = 30
    GENRE = 31
    FRAME_RATE = 32
    VIDEO_BIT_RATE = 33
    VIDEO_FORMAT = 34
    RATING = 35
    TAGS = 36
    MD5 = 37
    SHA1 = 38
    SHA256 = 39
    CRC32 = 40
    SIZE_ON_DISK = 41
    DESCRIPTION = 42
    VERSION = 43
    PRODUCT_NAME = 44
    PRODUCT_VERSION = 45
    COMPANY = 46
    KIND = 47
    FILE_NAME_LENGTH = 48
    FULL_PATH_LENGTH = 49
    SUBJECT = 50
    AUTHORS = 51
    DATE_TAKEN = 52
    SOFTWARE = 53
    DATE_ACQUIRED = 54
    COPYRIGHT = 55
    IMAGE_ID = 56
    HORIZONTAL_RESOLUTION = 57
    VERTICAL_RESOLUTION = 58
    COMPRESSION = 59
    RESOLUTION_UNIT = 60
    COLOR_REPRESENTATION = 61
    COMPRESSED_BITS_PER_PIXEL = 62
    CAMERA_MAKER = 63
    CAMERA_MODEL = 64
    F_STOP = 65
    EXPOSURE_TIME = 66
    ISO_SPEED = 67
    EXPOSURE_BIAS = 68
    FOCAL_LENGTH = 69
    MAX_APERTURE = 70
    METERING_MODE = 71
    SUBJECT_DISTANCE = 72
    FLASH_MODE = 73
    FLASH_ENERGY = 74
    LENS_MAKER = 76
    LENS_MODEL = 77
    FLASH_MAKER = 78
    FLASH_MODEL = 79
    CAMERA_SERIAL_NUMBER = 80
    CONTRAST = 81
    BRIGHTNESS = 82
    LIGHT_SOURCE = 83
    EXPOSURE_PROGRAM = 84
    SATURATION = 85
    SHARPNESS = 86
    WHITE_BALANCE = 87
    PHOTOMETRIC_INTERPRETATION = 88
    DIGITAL_ZOOM = 89
    EXIF_VERSION = 90
    LATITUDE = 91
    LONGITUDE = 92
    ALTITUDE = 93
    SUBTITLE = 94
    TOTAL_BIT_RATE = 95
    DIRECTORS = 96
    PRODUCERS = 97
    WRITERS = 98
    PUBLISHER = 99
    CONTENT_DISTRIBUTOR = 100
    DATE_ENCODED = 101
    ENCODED_BY = 102
    AUTHOR_URL = 103
    PROMOTION_URL = 104
    OFFLINE_AVAILABILITY = 105
    OFFLINE_STATUS = 106
    SHARED_WITH = 107
    OWNER = 108
    COMPUTER = 109
    ALBUM_ARTIST = 110
    PARENTAL_RATING_REASON = 111
    COMPOSER = 112
    CONDUCTOR = 113
    CONTENT_GROUP_DESCRIPTION = 114
    MOOD = 115
    PART_OF_SET = 116
    INITIAL_KEY = 117
    BEATS_PER_MINUTE = 118
    PROTECTED = 119
    PART_OF_A_COMPILATION = 120
    PARENTAL_RATING = 121
    PERIOD = 122
    PEOPLE = 123
    CATEGORY = 124
    CONTENT_STATUS = 125
    DOCUMENT_CONTENT_TYPE = 126
    PAGE_COUNT = 127
    WORD_COUNT = 128
    CHARACTER_COUNT = 129
    LINE_COUNT = 130
    PARAGRAPH_COUNT = 131
    TEMPLATE = 132
    SCALE = 133
    LINKS_DIRTY = 134
    LANGUAGE = 135
    LAST_AUTHOR = 136
    REVISION_NUMBER = 137
    VERSION_NUMBER = 138
    MANAGER = 139
    DATE_CONTENT_CREATED = 140
    DATE_SAVED = 141
    DATE_PRINTED = 142
    TOTAL_EDITING_TIME = 143
    ORIGINAL_FILE_NAME = 144
    DATE_RELEASED = 145
    SLIDE_COUNT = 146
    NOTE_COUNT = 147
    HIDDEN_SLIDE_COUNT = 148
    PRESENTATION_FORMAT = 149
    TRADEMARKS = 150
    DISPLAY_NAME = 151
    FILE_NAME_LENGTH_IN_UTF8_BYTES = 152
    FULL_PATH_LENGTH_IN_UTF8_BYTES = 153
    CHILD_COUNT = 154
    CHILD_FOLDER_COUNT = 155
    CHILD_FILE_COUNT = 156
    CHILD_COUNT_FROM_DISK = 157
    CHILD_FOLDER_COUNT_FROM_DISK = 158
    CHILD_FILE_COUNT_FROM_DISK = 159
    FOLDER_DEPTH = 160
    TOTAL_SIZE = 161
    TOTAL_SIZE_ON_DISK = 162
    DATE_CHANGED = 163
    HARD_LINK_COUNT = 164
    DELETE_PENDING = 165
    IS_DIRECTORY = 166
    ALTERNATE_DATA_STREAM_COUNT = 167
    ALTERNATE_DATA_STREAM_NAMES = 168
    TOTAL_ALTERNATE_DATA_STREAM_SIZE = 169
    TOTAL_ALTERNATE_DATA_STREAM_SIZE_ON_DISK = 170
    COMPRESSED_SIZE = 171
    COMPRESSION_FORMAT = 172
    COMPRESSION_UNIT_SHIFT = 173
    COMPRESSION_CHUNK_SHIFT = 174
    COMPRESSION_CLUSTER_SHIFT = 175
    COMPRESSION_RATIO = 176
    REPARSE_TAG = 177
    REMOTE_PROTOCOL = 178
    REMOTE_PROTOCOL_VERSION = 179
    REMOTE_PROTOCOL_FLAGS = 180
    LOGICAL_BYTES_PER_SECTOR = 181
    PHYSICAL_BYTES_PER_SECTOR_FOR_ATOMICITY = 182
    PHYSICAL_BYTES_PER_SECTOR_FOR_PERFORMANCE = 183
    EFFECTIVE_PHYSICAL_BYTES_PER_SECTOR_FOR_ATOMICITY = 184
    FILE_STORAGE_INFO_FLAGS = 185
    BYTE_OFFSET_FOR_SECTOR_ALIGNMENT = 186
    BYTE_OFFSET_FOR_PARTITION_ALIGNMENT = 187
    ALIGNMENT_REQUIREMENT = 188
    VOLUME_SERIAL_NUMBER = 189
    FILE_ID = 190
    FRAME_COUNT = 191
    CLUSTER_SIZE = 192
    SECTOR_SIZE = 193
    AVAILABLE_FREE_DISK_SIZE = 194
    FREE_DISK_SIZE = 195
    TOTAL_DISK_SIZE = 196
    MAXIMUM_COMPONENT_LENGTH = 198
    FILE_SYSTEM_FLAGS = 199
    FILE_SYSTEM = 200
    ORIENTATION = 201
    END_OF_FILE = 202
    SHORT_NAME = 203
    SHORT_FULL_PATH = 204
    ENCRYPTION_STATUS = 205
    HARD_LINK_FILE_NAMES = 206
    INDEX_TYPE = 207
    DRIVE_TYPE = 208
    BINARY_TYPE = 209
    REGEX_MATCH_0 = 210
    REGEX_MATCH_1 = 211
    REGEX_MATCH_2 = 212
    REGEX_MATCH_3 = 213
    REGEX_MATCH_4 = 214
    REGEX_MATCH_5 = 215
    REGEX_MATCH_6 = 216
    REGEX_MATCH_7 = 217
    REGEX_MATCH_8 = 218
    REGEX_MATCH_9 = 219
    SIBLING_COUNT = 220
    SIBLING_FOLDER_COUNT = 221
    SIBLING_FILE_COUNT = 222
    INDEX_NUMBER = 223
    SHORTCUT_TARGET = 224
    OUT_OF_DATE = 225
    INCUR_SEEK_PENALTY = 226
    PLAIN_TEXT_LINE_COUNT = 227
    APERTURE = 228
    MAKER_NOTE = 229
    RELATED_SOUND_FILE = 230
    SHUTTER_SPEED = 231
    TRANSCODED_FOR_SYNC = 232
    CASE_SENSITIVE_DIR = 233
    DATE_INDEXED = 234
    NAME_FREQUENCY = 235
    SIZE_FREQUENCY = 236
    EXTENSION_FREQUENCY = 237
    REGEX_MATCHES = 238
    URL = 239
    FULL_PATH = 240
    PARENT_FILE_ID = 241
    SHA512 = 242
    SHA384 = 243
    CRC64 = 244
    FIRST_BYTE = 245
    FIRST_2_BYTES = 246
    FIRST_4_BYTES = 247
    FIRST_8_BYTES = 248
    FIRST_16_BYTES = 249
    FIRST_32_BYTES = 250
    FIRST_64_BYTES = 251
    FIRST_128_BYTES = 252
    LAST_BYTE = 253
    LAST_2_BYTES = 254
    LAST_4_BYTES = 255
    LAST_8_BYTES = 256
    LAST_16_BYTES = 257
    LAST_32_BYTES = 258
    LAST_64_BYTES = 259
    LAST_128_BYTES = 260
    BYTE_ORDER_MARK = 261
    VOLUME_LABEL = 262
    FILE_LIST_FULL_PATH = 263
    DISPLAY_FULL_PATH = 264
    PARSE_NAME = 265
    PARSE_FULL_PATH = 266
    STEM = 267
    SHELL_ATTRIBUTES = 268
    IS_FOLDER = 269
    VALID_UTF8 = 270
    STEM_LENGTH = 271
    EXTENSION_LENGTH = 272
    PATH_PART_LENGTH = 273
    TIME_MODIFIED = 274
    TIME_CREATED = 275
    TIME_ACCESSED = 276
    DAY_MODIFIED = 277
    DAY_CREATED = 278
    DAY_ACCESSED = 279
    PARENT_NAME = 280
    REPARSE_TARGET = 281
    DESCENDANT_COUNT = 282
    DESCENDANT_FOLDER_COUNT = 283
    DESCENDANT_FILE_COUNT = 284
    FROM = 285
    TO = 286
    DATE_RECEIVED = 287
    DATE_SENT = 288
    CONTAINER_FILENAMES = 289
    CONTAINER_FILE_COUNT = 290
    CUSTOM_PROPERTY_0 = 291
    CUSTOM_PROPERTY_1 = 292
    CUSTOM_PROPERTY_2 = 293
    CUSTOM_PROPERTY_3 = 294
    CUSTOM_PROPERTY_4 = 295
    CUSTOM_PROPERTY_5 = 296
    CUSTOM_PROPERTY_6 = 297
    CUSTOM_PROPERTY_7 = 298
    CUSTOM_PROPERTY_8 = 299
    CUSTOM_PROPERTY_9 = 300
    ALLOCATION_SIZE = 301
    SFV_CRC32 = 302
    MD5SUM_MD5 = 303
    SHA1SUM_SHA1 = 304
    SHA256SUM_SHA256 = 305
    SFV_PASS = 306
    MD5SUM_PASS = 307
    SHA1SUM_PASS = 308
    SHA256SUM_PASS = 309
    ALTERNATE_DATA_STREAM_ANSI = 310
    ALTERNATE_DATA_STREAM_UTF8 = 311
    ALTERNATE_DATA_STREAM_UTF16LE = 312
    ALTERNATE_DATA_STREAM_UTF16BE = 313
    ALTERNATE_DATA_STREAM_TEXT_PLAIN = 314
    ALTERNATE_DATA_STREAM_HEX = 315
    PERCEIVED_TYPE = 316
    CONTENT_TYPE = 317
    OPENED_BY = 318
    TARGET_MACHINE = 319
    SHA512SUM_SHA512 = 320
    SHA512SUM_PASS = 321
    PARENT_PATH = 322
    FIRST_256_BYTES = 323
    FIRST_512_BYTES = 324
    LAST_256_BYTES = 325
    LAST_512_BYTES = 326
    INDEX_ONLINE = 327
    COLUMN_0 = 328
    COLUMN_1 = 329
    COLUMN_2 = 330
    COLUMN_3 = 331
    COLUMN_4 = 332
    COLUMN_5 = 333
    COLUMN_6 = 334
    COLUMN_7 = 335
    COLUMN_8 = 336
    COLUMN_9 = 337
    COLUMN_A = 338
    COLUMN_B = 339
    COLUMN_C = 340
    COLUMN_D = 341
    COLUMN_E = 342
    COLUMN_F = 343
    ZONE_ID = 344
    REFERRER_URL = 345
    HOST_URL = 346
    CHARACTER_ENCODING = 347
    ROOT_NAME = 348
    USED_DISK_SIZE = 349
    VOLUME_PATH = 350
    MAX_CHILD_DEPTH = 351
    TOTAL_CHILD_SIZE = 352
    ROW = 353
    CHILD_OCCURRENCE_COUNT = 354
    VOLUME_NAME = 355
    DESCENDANT_OCCURRENCE_COUNT = 356
    OBJECT_ID = 357
    BIRTH_VOLUME_ID = 358
    BIRTH_OBJECT_ID = 359
    DOMAIN_ID = 360
    FOLDER_DATA_CRC32 = 361
    FOLDER_DATA_CRC64 = 362
    FOLDER_DATA_MD5 = 363
    FOLDER_DATA_SHA1 = 364
    FOLDER_DATA_SHA256 = 365
    FOLDER_DATA_SHA512 = 366
    FOLDER_DATA_AND_NAMES_CRC32 = 367
    FOLDER_DATA_AND_NAMES_CRC64 = 368
    FOLDER_DATA_AND_NAMES_MD5 = 369
    FOLDER_DATA_AND_NAMES_SHA1 = 370
    FOLDER_DATA_AND_NAMES_SHA256 = 371
    FOLDER_DATA_AND_NAMES_SHA512 = 372
    FOLDER_NAMES_CRC32 = 373
    FOLDER_NAMES_CRC64 = 374
    FOLDER_NAMES_MD5 = 375
    FOLDER_NAMES_SHA1 = 376
    FOLDER_NAMES_SHA256 = 377
    FOLDER_NAMES_SHA512 = 378
    FOLDER_DATA_CRC32_FROM_DISK = 379
    FOLDER_DATA_CRC64_FROM_DISK = 380
    FOLDER_DATA_MD5_FROM_DISK = 381
    FOLDER_DATA_SHA1_FROM_DISK = 382
    FOLDER_DATA_SHA256_FROM_DISK = 383
    FOLDER_DATA_SHA512_FROM_DISK = 384
    FOLDER_DATA_AND_NAMES_CRC32_FROM_DISK = 385
    FOLDER_DATA_AND_NAMES_CRC64_FROM_DISK = 386
    FOLDER_DATA_AND_NAMES_MD5_FROM_DISK = 387
    FOLDER_DATA_AND_NAMES_SHA1_FROM_DISK = 388
    FOLDER_DATA_AND_NAMES_SHA256_FROM_DISK = 389
    FOLDER_DATA_AND_NAMES_SHA512_FROM_DISK = 390
    FOLDER_NAMES_CRC32_FROM_DISK = 391
    FOLDER_NAMES_CRC64_FROM_DISK = 392
    FOLDER_NAMES_MD5_FROM_DISK = 393
    FOLDER_NAMES_SHA1_FROM_DISK = 394
    FOLDER_NAMES_SHA256_FROM_DISK = 395
    FOLDER_NAMES_SHA512_FROM_DISK = 396
    LONG_NAME = 397
    LONG_FULL_PATH = 398
    DIGITAL_SIGNATURE_NAME = 399
    DIGITAL_SIGNATURE_TIMESTAMP = 400
    AUDIO_TRACK_COUNT = 401
    VIDEO_TRACK_COUNT = 402
    SUBTITLE_TRACK_COUNT = 403
    NETWORK_INDEX_HOST = 404
    ORIGINAL_LOCATION = 405
    DATE_DELETED = 406
    STATUS = 407
    VORBIS_COMMENT = 408
    QUICKTIME_METADATA = 409
    PARENT_SIZE = 410
    ROOT_SIZE = 411
    OPENS_WITH = 412
    RANDOMIZE = 413
    ICON = 414
    THUMBNAIL = 415
    CONTENT = 416
    SEPARATOR = 417

PropertyIdToValueTypeMap = {
    PropertyId.NAME: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.PATH: PropertyValueType.PSTRING_FOLDER_REFERENCE,
    PropertyId.SIZE: PropertyValueType.UINT64,
    PropertyId.EXTENSION: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.TYPE: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.DATE_MODIFIED: PropertyValueType.UINT64,
    PropertyId.DATE_CREATED: PropertyValueType.UINT64,
    PropertyId.DATE_ACCESSED: PropertyValueType.UINT64,
    PropertyId.ATTRIBUTES: PropertyValueType.DWORD,
    PropertyId.DATE_RECENTLY_CHANGED: PropertyValueType.UINT64,
    PropertyId.RUN_COUNT: PropertyValueType.DWORD,
    PropertyId.DATE_RUN: PropertyValueType.UINT64,
    PropertyId.FILE_LIST_FILENAME: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.WIDTH: PropertyValueType.DWORD,
    PropertyId.HEIGHT: PropertyValueType.DWORD,
    PropertyId.DIMENSIONS: PropertyValueType.DIMENSIONS,
    PropertyId.ASPECT_RATIO: PropertyValueType.DWORD_FIXED_Q1K,
    PropertyId.BIT_DEPTH: PropertyValueType.BYTE,
    PropertyId.LENGTH: PropertyValueType.UINT64,
    PropertyId.AUDIO_SAMPLE_RATE: PropertyValueType.DWORD,
    PropertyId.AUDIO_CHANNELS: PropertyValueType.DWORD,
    PropertyId.AUDIO_BITS_PER_SAMPLE: PropertyValueType.DWORD,
    PropertyId.AUDIO_BIT_RATE: PropertyValueType.DWORD,
    PropertyId.AUDIO_FORMAT: PropertyValueType.PSTRING,
    PropertyId.FILE_SIGNATURE: PropertyValueType.DWORD_GET_TEXT,
    PropertyId.TITLE: PropertyValueType.PSTRING,
    PropertyId.ARTIST: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.ALBUM: PropertyValueType.PSTRING,
    PropertyId.YEAR: PropertyValueType.DWORD,
    PropertyId.COMMENT: PropertyValueType.PSTRING,
    PropertyId.TRACK: PropertyValueType.DWORD,
    PropertyId.GENRE: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.FRAME_RATE: PropertyValueType.DWORD_FIXED_Q1K,
    PropertyId.VIDEO_BIT_RATE: PropertyValueType.DWORD,
    PropertyId.VIDEO_FORMAT: PropertyValueType.PSTRING,
    PropertyId.RATING: PropertyValueType.BYTE,
    PropertyId.TAGS: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.MD5: PropertyValueType.BLOB8,
    PropertyId.SHA1: PropertyValueType.BLOB8,
    PropertyId.SHA256: PropertyValueType.BLOB8,
    PropertyId.CRC32: PropertyValueType.BLOB8,
    PropertyId.SIZE_ON_DISK: PropertyValueType.UINT64,
    PropertyId.DESCRIPTION: PropertyValueType.PSTRING,
    PropertyId.VERSION: PropertyValueType.PSTRING,
    PropertyId.PRODUCT_NAME: PropertyValueType.PSTRING,
    PropertyId.PRODUCT_VERSION: PropertyValueType.PSTRING,
    PropertyId.COMPANY: PropertyValueType.PSTRING,
    PropertyId.KIND: PropertyValueType.PSTRING,
    PropertyId.FILE_NAME_LENGTH: PropertyValueType.SIZE_T,
    PropertyId.FULL_PATH_LENGTH: PropertyValueType.SIZE_T,
    PropertyId.SUBJECT: PropertyValueType.PSTRING,
    PropertyId.AUTHORS: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.DATE_TAKEN: PropertyValueType.UINT64,
    PropertyId.SOFTWARE: PropertyValueType.PSTRING,
    PropertyId.DATE_ACQUIRED: PropertyValueType.UINT64,
    PropertyId.COPYRIGHT: PropertyValueType.PSTRING,
    PropertyId.IMAGE_ID: PropertyValueType.PSTRING,
    PropertyId.HORIZONTAL_RESOLUTION: PropertyValueType.DWORD,
    PropertyId.VERTICAL_RESOLUTION: PropertyValueType.DWORD,
    PropertyId.COMPRESSION: PropertyValueType.WORD,
    PropertyId.RESOLUTION_UNIT: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.COLOR_REPRESENTATION: PropertyValueType.WORD,
    PropertyId.COMPRESSED_BITS_PER_PIXEL: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.CAMERA_MAKER: PropertyValueType.PSTRING,
    PropertyId.CAMERA_MODEL: PropertyValueType.PSTRING,
    PropertyId.F_STOP: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.EXPOSURE_TIME: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.ISO_SPEED: PropertyValueType.WORD,
    PropertyId.EXPOSURE_BIAS: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.FOCAL_LENGTH: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.MAX_APERTURE: PropertyValueType.INT32_FIXED_Q1M,
    PropertyId.METERING_MODE: PropertyValueType.WORD,
    PropertyId.SUBJECT_DISTANCE: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.FLASH_MODE: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.FLASH_ENERGY: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.LENS_MAKER: PropertyValueType.PSTRING,
    PropertyId.LENS_MODEL: PropertyValueType.PSTRING,
    PropertyId.FLASH_MAKER: PropertyValueType.PSTRING,
    PropertyId.FLASH_MODEL: PropertyValueType.PSTRING,
    PropertyId.CAMERA_SERIAL_NUMBER: PropertyValueType.PSTRING,
    PropertyId.CONTRAST: PropertyValueType.DWORD,
    PropertyId.BRIGHTNESS: PropertyValueType.INT32_FIXED_Q1M,
    PropertyId.LIGHT_SOURCE: PropertyValueType.DWORD,
    PropertyId.EXPOSURE_PROGRAM: PropertyValueType.DWORD,
    PropertyId.SATURATION: PropertyValueType.DWORD,
    PropertyId.SHARPNESS: PropertyValueType.DWORD,
    PropertyId.WHITE_BALANCE: PropertyValueType.DWORD,
    PropertyId.PHOTOMETRIC_INTERPRETATION: PropertyValueType.WORD,
    PropertyId.DIGITAL_ZOOM: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.EXIF_VERSION: PropertyValueType.PSTRING,
    PropertyId.LATITUDE: PropertyValueType.INT32_FIXED_Q1M,
    PropertyId.LONGITUDE: PropertyValueType.INT32_FIXED_Q1M,
    PropertyId.ALTITUDE: PropertyValueType.INT32_FIXED_Q1M,
    PropertyId.SUBTITLE: PropertyValueType.PSTRING,
    PropertyId.TOTAL_BIT_RATE: PropertyValueType.DWORD,
    PropertyId.DIRECTORS: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.PRODUCERS: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.WRITERS: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.PUBLISHER: PropertyValueType.PSTRING,
    PropertyId.CONTENT_DISTRIBUTOR: PropertyValueType.PSTRING,
    PropertyId.DATE_ENCODED: PropertyValueType.UINT64,
    PropertyId.ENCODED_BY: PropertyValueType.PSTRING,
    PropertyId.AUTHOR_URL: PropertyValueType.PSTRING,
    PropertyId.PROMOTION_URL: PropertyValueType.PSTRING,
    PropertyId.OFFLINE_AVAILABILITY: PropertyValueType.DWORD,
    PropertyId.OFFLINE_STATUS: PropertyValueType.DWORD,
    PropertyId.SHARED_WITH: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.OWNER: PropertyValueType.PSTRING,
    PropertyId.COMPUTER: PropertyValueType.PSTRING,
    PropertyId.ALBUM_ARTIST: PropertyValueType.PSTRING,
    PropertyId.PARENTAL_RATING_REASON: PropertyValueType.PSTRING,
    PropertyId.COMPOSER: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.CONDUCTOR: PropertyValueType.PSTRING,
    PropertyId.CONTENT_GROUP_DESCRIPTION: PropertyValueType.PSTRING,
    PropertyId.MOOD: PropertyValueType.PSTRING,
    PropertyId.PART_OF_SET: PropertyValueType.PSTRING,
    PropertyId.INITIAL_KEY: PropertyValueType.PSTRING,
    PropertyId.BEATS_PER_MINUTE: PropertyValueType.PSTRING,
    PropertyId.PROTECTED: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.PART_OF_A_COMPILATION: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.PARENTAL_RATING: PropertyValueType.PSTRING,
    PropertyId.PERIOD: PropertyValueType.PSTRING,
    PropertyId.PEOPLE: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.CATEGORY: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.CONTENT_STATUS: PropertyValueType.PSTRING,
    PropertyId.DOCUMENT_CONTENT_TYPE: PropertyValueType.PSTRING,
    PropertyId.PAGE_COUNT: PropertyValueType.DWORD,
    PropertyId.WORD_COUNT: PropertyValueType.DWORD,
    PropertyId.CHARACTER_COUNT: PropertyValueType.DWORD,
    PropertyId.LINE_COUNT: PropertyValueType.DWORD,
    PropertyId.PARAGRAPH_COUNT: PropertyValueType.DWORD,
    PropertyId.TEMPLATE: PropertyValueType.PSTRING,
    PropertyId.SCALE: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.LINKS_DIRTY: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.LANGUAGE: PropertyValueType.PSTRING,
    PropertyId.LAST_AUTHOR: PropertyValueType.PSTRING,
    PropertyId.REVISION_NUMBER: PropertyValueType.PSTRING,
    PropertyId.VERSION_NUMBER: PropertyValueType.PSTRING,
    PropertyId.MANAGER: PropertyValueType.PSTRING,
    PropertyId.DATE_CONTENT_CREATED: PropertyValueType.UINT64,
    PropertyId.DATE_SAVED: PropertyValueType.UINT64,
    PropertyId.DATE_PRINTED: PropertyValueType.UINT64,
    PropertyId.TOTAL_EDITING_TIME: PropertyValueType.UINT64,
    PropertyId.ORIGINAL_FILE_NAME: PropertyValueType.PSTRING,
    PropertyId.DATE_RELEASED: PropertyValueType.PSTRING,
    PropertyId.SLIDE_COUNT: PropertyValueType.DWORD,
    PropertyId.NOTE_COUNT: PropertyValueType.DWORD,
    PropertyId.HIDDEN_SLIDE_COUNT: PropertyValueType.DWORD,
    PropertyId.PRESENTATION_FORMAT: PropertyValueType.PSTRING,
    PropertyId.TRADEMARKS: PropertyValueType.PSTRING,
    PropertyId.DISPLAY_NAME: PropertyValueType.PSTRING,
    PropertyId.FILE_NAME_LENGTH_IN_UTF8_BYTES: PropertyValueType.SIZE_T,
    PropertyId.FULL_PATH_LENGTH_IN_UTF8_BYTES: PropertyValueType.SIZE_T,
    PropertyId.CHILD_COUNT: PropertyValueType.SIZE_T,
    PropertyId.CHILD_FOLDER_COUNT: PropertyValueType.SIZE_T,
    PropertyId.CHILD_FILE_COUNT: PropertyValueType.SIZE_T,
    PropertyId.CHILD_COUNT_FROM_DISK: PropertyValueType.SIZE_T,
    PropertyId.CHILD_FOLDER_COUNT_FROM_DISK: PropertyValueType.SIZE_T,
    PropertyId.CHILD_FILE_COUNT_FROM_DISK: PropertyValueType.SIZE_T,
    PropertyId.FOLDER_DEPTH: PropertyValueType.SIZE_T,
    PropertyId.TOTAL_SIZE: PropertyValueType.UINT64,
    PropertyId.TOTAL_SIZE_ON_DISK: PropertyValueType.UINT64,
    PropertyId.DATE_CHANGED: PropertyValueType.UINT64,
    PropertyId.HARD_LINK_COUNT: PropertyValueType.DWORD,
    PropertyId.DELETE_PENDING: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.IS_DIRECTORY: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.ALTERNATE_DATA_STREAM_COUNT: PropertyValueType.DWORD,
    PropertyId.ALTERNATE_DATA_STREAM_NAMES: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.TOTAL_ALTERNATE_DATA_STREAM_SIZE: PropertyValueType.UINT64,
    PropertyId.TOTAL_ALTERNATE_DATA_STREAM_SIZE_ON_DISK: PropertyValueType.UINT64,
    PropertyId.COMPRESSED_SIZE: PropertyValueType.UINT64,
    PropertyId.COMPRESSION_FORMAT: PropertyValueType.WORD,
    PropertyId.COMPRESSION_UNIT_SHIFT: PropertyValueType.BYTE,
    PropertyId.COMPRESSION_CHUNK_SHIFT: PropertyValueType.BYTE,
    PropertyId.COMPRESSION_CLUSTER_SHIFT: PropertyValueType.BYTE,
    PropertyId.COMPRESSION_RATIO: PropertyValueType.BYTE,
    PropertyId.REPARSE_TAG: PropertyValueType.DWORD,
    PropertyId.REMOTE_PROTOCOL: PropertyValueType.DWORD,
    PropertyId.REMOTE_PROTOCOL_VERSION: PropertyValueType.PSTRING,
    PropertyId.REMOTE_PROTOCOL_FLAGS: PropertyValueType.DWORD,
    PropertyId.LOGICAL_BYTES_PER_SECTOR: PropertyValueType.DWORD,
    PropertyId.PHYSICAL_BYTES_PER_SECTOR_FOR_ATOMICITY: PropertyValueType.DWORD,
    PropertyId.PHYSICAL_BYTES_PER_SECTOR_FOR_PERFORMANCE: PropertyValueType.DWORD,
    PropertyId.EFFECTIVE_PHYSICAL_BYTES_PER_SECTOR_FOR_ATOMICITY: PropertyValueType.DWORD,
    PropertyId.FILE_STORAGE_INFO_FLAGS: PropertyValueType.DWORD,
    PropertyId.BYTE_OFFSET_FOR_SECTOR_ALIGNMENT: PropertyValueType.DWORD,
    PropertyId.BYTE_OFFSET_FOR_PARTITION_ALIGNMENT: PropertyValueType.DWORD,
    PropertyId.ALIGNMENT_REQUIREMENT: PropertyValueType.DWORD,
    PropertyId.VOLUME_SERIAL_NUMBER: PropertyValueType.UINT64,
    PropertyId.FILE_ID: PropertyValueType.UINT128,
    PropertyId.FRAME_COUNT: PropertyValueType.DWORD,
    PropertyId.CLUSTER_SIZE: PropertyValueType.DWORD,
    PropertyId.SECTOR_SIZE: PropertyValueType.DWORD,
    PropertyId.AVAILABLE_FREE_DISK_SIZE: PropertyValueType.UINT64,
    PropertyId.FREE_DISK_SIZE: PropertyValueType.UINT64,
    PropertyId.TOTAL_DISK_SIZE: PropertyValueType.UINT64,
    PropertyId.MAXIMUM_COMPONENT_LENGTH: PropertyValueType.DWORD,
    PropertyId.FILE_SYSTEM_FLAGS: PropertyValueType.DWORD,
    PropertyId.FILE_SYSTEM: PropertyValueType.PSTRING,
    PropertyId.ORIENTATION: PropertyValueType.WORD,
    PropertyId.END_OF_FILE: PropertyValueType.UINT64,
    PropertyId.SHORT_NAME: PropertyValueType.PSTRING,
    PropertyId.SHORT_FULL_PATH: PropertyValueType.PSTRING,
    PropertyId.ENCRYPTION_STATUS: PropertyValueType.DWORD,
    PropertyId.HARD_LINK_FILE_NAMES: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.INDEX_TYPE: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.DRIVE_TYPE: PropertyValueType.DWORD,
    PropertyId.BINARY_TYPE: PropertyValueType.DWORD,
    PropertyId.REGEX_MATCH_0: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_1: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_2: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_3: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_4: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_5: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_6: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_7: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_8: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_9: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.SIBLING_COUNT: PropertyValueType.SIZE_T,
    PropertyId.SIBLING_FOLDER_COUNT: PropertyValueType.SIZE_T,
    PropertyId.SIBLING_FILE_COUNT: PropertyValueType.SIZE_T,
    PropertyId.INDEX_NUMBER: PropertyValueType.SIZE_T,
    PropertyId.SHORTCUT_TARGET: PropertyValueType.PSTRING,
    PropertyId.OUT_OF_DATE: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.INCUR_SEEK_PENALTY: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.PLAIN_TEXT_LINE_COUNT: PropertyValueType.DWORD,
    PropertyId.APERTURE: PropertyValueType.INT32_FIXED_Q1M,
    PropertyId.MAKER_NOTE: PropertyValueType.PSTRING,
    PropertyId.RELATED_SOUND_FILE: PropertyValueType.PSTRING,
    PropertyId.SHUTTER_SPEED: PropertyValueType.INT32_FIXED_Q1K,
    PropertyId.TRANSCODED_FOR_SYNC: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.CASE_SENSITIVE_DIR: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.DATE_INDEXED: PropertyValueType.UINT64,
    PropertyId.NAME_FREQUENCY: PropertyValueType.SIZE_T,
    PropertyId.SIZE_FREQUENCY: PropertyValueType.SIZE_T,
    PropertyId.EXTENSION_FREQUENCY: PropertyValueType.SIZE_T,
    PropertyId.REGEX_MATCHES: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.URL: PropertyValueType.PSTRING,
    PropertyId.FULL_PATH: PropertyValueType.PSTRING_FILE_OR_FOLDER_REFERENCE,
    PropertyId.PARENT_FILE_ID: PropertyValueType.UINT128,
    PropertyId.SHA512: PropertyValueType.BLOB8,
    PropertyId.SHA384: PropertyValueType.BLOB8,
    PropertyId.CRC64: PropertyValueType.BLOB8,
    PropertyId.FIRST_BYTE: PropertyValueType.BLOB8,
    PropertyId.FIRST_2_BYTES: PropertyValueType.BLOB8,
    PropertyId.FIRST_4_BYTES: PropertyValueType.BLOB8,
    PropertyId.FIRST_8_BYTES: PropertyValueType.BLOB8,
    PropertyId.FIRST_16_BYTES: PropertyValueType.BLOB8,
    PropertyId.FIRST_32_BYTES: PropertyValueType.BLOB8,
    PropertyId.FIRST_64_BYTES: PropertyValueType.BLOB8,
    PropertyId.FIRST_128_BYTES: PropertyValueType.BLOB8,
    PropertyId.LAST_BYTE: PropertyValueType.BLOB8,
    PropertyId.LAST_2_BYTES: PropertyValueType.BLOB8,
    PropertyId.LAST_4_BYTES: PropertyValueType.BLOB8,
    PropertyId.LAST_8_BYTES: PropertyValueType.BLOB8,
    PropertyId.LAST_16_BYTES: PropertyValueType.BLOB8,
    PropertyId.LAST_32_BYTES: PropertyValueType.BLOB8,
    PropertyId.LAST_64_BYTES: PropertyValueType.BLOB8,
    PropertyId.LAST_128_BYTES: PropertyValueType.BLOB8,
    PropertyId.BYTE_ORDER_MARK: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.VOLUME_LABEL: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.FILE_LIST_FULL_PATH: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.DISPLAY_FULL_PATH: PropertyValueType.PSTRING,
    PropertyId.PARSE_NAME: PropertyValueType.PSTRING,
    PropertyId.PARSE_FULL_PATH: PropertyValueType.PSTRING,
    PropertyId.STEM: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.SHELL_ATTRIBUTES: PropertyValueType.DWORD,
    PropertyId.IS_FOLDER: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.VALID_UTF8: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.STEM_LENGTH: PropertyValueType.SIZE_T,
    PropertyId.EXTENSION_LENGTH: PropertyValueType.SIZE_T,
    PropertyId.PATH_PART_LENGTH: PropertyValueType.SIZE_T,
    PropertyId.TIME_MODIFIED: PropertyValueType.DWORD,
    PropertyId.TIME_CREATED: PropertyValueType.DWORD,
    PropertyId.TIME_ACCESSED: PropertyValueType.DWORD,
    PropertyId.DAY_MODIFIED: PropertyValueType.DWORD,
    PropertyId.DAY_CREATED: PropertyValueType.DWORD,
    PropertyId.DAY_ACCESSED: PropertyValueType.DWORD,
    PropertyId.PARENT_NAME: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.REPARSE_TARGET: PropertyValueType.PSTRING,
    PropertyId.DESCENDANT_COUNT: PropertyValueType.SIZE_T,
    PropertyId.DESCENDANT_FOLDER_COUNT: PropertyValueType.SIZE_T,
    PropertyId.DESCENDANT_FILE_COUNT: PropertyValueType.SIZE_T,
    PropertyId.FROM: PropertyValueType.PSTRING,
    PropertyId.TO: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.DATE_RECEIVED: PropertyValueType.UINT64,
    PropertyId.DATE_SENT: PropertyValueType.UINT64,
    PropertyId.CONTAINER_FILENAMES: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.CONTAINER_FILE_COUNT: PropertyValueType.DWORD,
    PropertyId.CUSTOM_PROPERTY_0: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_1: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_2: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_3: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_4: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_5: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_6: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_7: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_8: PropertyValueType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_9: PropertyValueType.PSTRING,
    PropertyId.ALLOCATION_SIZE: PropertyValueType.UINT64,
    PropertyId.SFV_CRC32: PropertyValueType.BLOB8,
    PropertyId.MD5SUM_MD5: PropertyValueType.BLOB8,
    PropertyId.SHA1SUM_SHA1: PropertyValueType.BLOB8,
    PropertyId.SHA256SUM_SHA256: PropertyValueType.BLOB8,
    PropertyId.SFV_PASS: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.MD5SUM_PASS: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.SHA1SUM_PASS: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.SHA256SUM_PASS: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.ALTERNATE_DATA_STREAM_ANSI: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_UTF8: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_UTF16LE: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_UTF16BE: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_TEXT_PLAIN: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_HEX: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.PERCEIVED_TYPE: PropertyValueType.PSTRING,
    PropertyId.CONTENT_TYPE: PropertyValueType.PSTRING,
    PropertyId.OPENED_BY: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.TARGET_MACHINE: PropertyValueType.WORD_GET_TEXT,
    PropertyId.SHA512SUM_SHA512: PropertyValueType.BLOB8,
    PropertyId.SHA512SUM_PASS: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.PARENT_PATH: PropertyValueType.PSTRING_FOLDER_REFERENCE,
    PropertyId.FIRST_256_BYTES: PropertyValueType.BLOB16,
    PropertyId.FIRST_512_BYTES: PropertyValueType.BLOB16,
    PropertyId.LAST_256_BYTES: PropertyValueType.BLOB16,
    PropertyId.LAST_512_BYTES: PropertyValueType.BLOB16,
    PropertyId.INDEX_ONLINE: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.COLUMN_0: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_1: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_2: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_3: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_4: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_5: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_6: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_7: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_8: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_9: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_A: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_B: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_C: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_D: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_E: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_F: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.ZONE_ID: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.REFERRER_URL: PropertyValueType.PSTRING,
    PropertyId.HOST_URL: PropertyValueType.PSTRING,
    PropertyId.CHARACTER_ENCODING: PropertyValueType.BYTE_GET_TEXT,
    PropertyId.ROOT_NAME: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.USED_DISK_SIZE: PropertyValueType.UINT64,
    PropertyId.VOLUME_PATH: PropertyValueType.PSTRING,
    PropertyId.MAX_CHILD_DEPTH: PropertyValueType.SIZE_T,
    PropertyId.TOTAL_CHILD_SIZE: PropertyValueType.UINT64,
    PropertyId.ROW: PropertyValueType.SIZE_T,
    PropertyId.CHILD_OCCURRENCE_COUNT: PropertyValueType.SIZE_T,
    PropertyId.VOLUME_NAME: PropertyValueType.PSTRING,
    PropertyId.DESCENDANT_OCCURRENCE_COUNT: PropertyValueType.SIZE_T,
    PropertyId.OBJECT_ID: PropertyValueType.BLOB8,
    PropertyId.BIRTH_VOLUME_ID: PropertyValueType.BLOB8,
    PropertyId.BIRTH_OBJECT_ID: PropertyValueType.BLOB8,
    PropertyId.DOMAIN_ID: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_CRC32: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_CRC64: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_MD5: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_SHA1: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_SHA256: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_SHA512: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_CRC32: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_CRC64: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_MD5: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA1: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA256: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA512: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_CRC32: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_CRC64: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_MD5: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA1: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA256: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA512: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_CRC32_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_CRC64_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_MD5_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_SHA1_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_SHA256_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_SHA512_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_CRC32_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_CRC64_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_MD5_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA1_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA256_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA512_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_CRC32_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_CRC64_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_MD5_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA1_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA256_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA512_FROM_DISK: PropertyValueType.BLOB8,
    PropertyId.LONG_NAME: PropertyValueType.PSTRING,
    PropertyId.LONG_FULL_PATH: PropertyValueType.PSTRING,
    PropertyId.DIGITAL_SIGNATURE_NAME: PropertyValueType.PSTRING,
    PropertyId.DIGITAL_SIGNATURE_TIMESTAMP: PropertyValueType.UINT64,
    PropertyId.AUDIO_TRACK_COUNT: PropertyValueType.DWORD,
    PropertyId.VIDEO_TRACK_COUNT: PropertyValueType.DWORD,
    PropertyId.SUBTITLE_TRACK_COUNT: PropertyValueType.DWORD,
    PropertyId.NETWORK_INDEX_HOST: PropertyValueType.PSTRING_STRING_REFERENCE,
    PropertyId.ORIGINAL_LOCATION: PropertyValueType.PSTRING,
    PropertyId.DATE_DELETED: PropertyValueType.UINT64,
    PropertyId.STATUS: PropertyValueType.BYTE,
    PropertyId.VORBIS_COMMENT: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.QUICKTIME_METADATA: PropertyValueType.PSTRING_MULTISTRING,
    PropertyId.PARENT_SIZE: PropertyValueType.UINT64,
    PropertyId.ROOT_SIZE: PropertyValueType.UINT64,
    PropertyId.OPENS_WITH: PropertyValueType.PSTRING,
    PropertyId.RANDOMIZE: PropertyValueType.SIZE_T,
    PropertyId.ICON: PropertyValueType.NULL,
    PropertyId.THUMBNAIL: PropertyValueType.NULL,
    PropertyId.CONTENT: PropertyValueType.PSTRING,
    PropertyId.SEPARATOR: PropertyValueType.NULL,
}
def PropertyIdToValueType(id: PropertyId) -> typing.Optional[PropertyValueType]:
    return PropertyIdToValueTypeMap.get(id, None)
#endregion

