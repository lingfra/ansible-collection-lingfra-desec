from ansible.errors import AnsibleFilterError


def parse_rrset_item(data):
    if not isinstance(data, dict):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type dict."
        )

    return {
        "subname": data["subname"],
        "type": data["type"],
        "ttl": data.get("ttl", 3600),
        "records": data.get("records", []),
    }


def parse_rrset_list(data):
    if not isinstance(data, list):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type list."
        )

    rrset_list = []

    for rrset in data:
        rrset_list.append(parse_rrset_item(rrset))

    return rrset_list


def parse_dns_domain_list(data):
    if not isinstance(data, list):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type list."
        )

    dns_domain_list = []

    for domain_list_item in data:
        dns_domain_list.append(
            {
                "name": domain_list_item["name"],
                "rrset_list": parse_rrset_list(domain_list_item["rrset_list"]),
            }
        )

    return dns_domain_list


# Register the filters
class FilterModule(object):
    def filters(self):
        return {
            "parse_dns_domain_list": parse_dns_domain_list,
        }
