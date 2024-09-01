#!/usr/bin/env python3
import re
from typing import Dict, Any

class DictClass:
    def to_dict(self) -> Dict[str, Any]:
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
        last_id_name = [key for key in cleaned_dict.keys() if re.match(id_pattern_second, key)][0]
        id_value = cleaned_dict.get(last_id_name)
        del cleaned_dict[last_id_name]
        cleaned_dict['id'] = id_value
        return cleaned_dict
