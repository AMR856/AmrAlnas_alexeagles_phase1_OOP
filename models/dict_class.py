#!/usr/bin/env python3
import datetime
import re
from typing import Dict, Any
import json

class DictClass:
    def to_dict(self) -> Dict[str, Any]:
        from .person import Person
        id_pattern_first = rf'^_{self.__class__.__name__}.*_id$'
        id_pattern_second = rf'.*{self.__class__.__name__.lower()}_id$'
        ids = [key for key in self.__dict__.keys() if re.match(id_pattern_first, key)]
        for key in list(self.__dict__.keys()):
            if key in ids and not self.__dict__[key]:
                del self.__dict__[key]
        cleaned_dict = {
            key.replace(f'_{self.__class__.__name__}__', ''): value
            for key, value in self.__dict__.items()
        }
        if issubclass(self.__class__, Person):
            cleaned_dict = {
                key.replace(f'_Person__', ''): value
                for key, value in cleaned_dict.items()
            }
        cleaned_dict = {k: v for k, v in cleaned_dict.items() if v is not None}
        last_id_name = [key for key in cleaned_dict.keys() if re.match(id_pattern_second, key)][0]
        id_value = cleaned_dict.get(last_id_name)
        del cleaned_dict[last_id_name]
        cleaned_dict['id'] = id_value
        return cleaned_dict

    @classmethod
    def json_saving(cls, *args) -> None:
        json_list = []
        if args:
            file_path = f'/mnt/h/oop_alex_eagles/data/{cls.__name__.lower()}.json'
            for arg in args:
                if arg is None:
                    return
                else:
                    object_dict = arg.to_dict()
                    for key in object_dict.keys():
                        if isinstance(object_dict[key], list):
                            replacing_list = []
                            value_list = object_dict[key]
                            for elm in value_list:
                                try:
                                    elm_dict_checker = elm.to_dict()
                                except Exception as err:
                                    continue
                                for elm_check_key in elm_dict_checker.keys():
                                    if isinstance(elm_dict_checker[elm_check_key], datetime.datetime):
                                        elm_dict_checker[elm_check_key] = elm_dict_checker[elm_check_key].strftime("%x")
                                replacing_list.append(elm_dict_checker)
                                object_dict[key] = replacing_list
                        elif isinstance(object_dict[key], datetime.datetime):
                            object_dict[key] = object_dict[key].strftime("%x")
                    json_list.append(object_dict)
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(json_list, file)
