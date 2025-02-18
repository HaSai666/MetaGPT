#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/24 19:05
@Author  : alexanderwu
@File    : startup.py
"""
import asyncio
import fire
from metagpt.software_company import SoftwareCompany
from metagpt.roles import ProjectManager, ProductManager, Architect, Engineer


async def startup(idea: str, investment: str = "$3.0", n_round: int = 5):
    """Run a startup. Be a boss."""
    company = SoftwareCompany()
    company.hire([ProductManager(), Architect(), ProjectManager(), Engineer(n_borg=5)])
    company.invest(investment)
    company.start_project(idea)
    await company.run(n_round=n_round)


def main(idea: str, investment: str = "$3.0"):
    """
    We are a software startup comprised of AI. By investing in us, you are empowering a future filled with limitless possibilities.
    :param idea: Your innovative idea, such as "Creating a snake game."
    :param investment: As an investor, you have the opportunity to contribute a certain dollar amount to this AI company.
    :return:
    """
    asyncio.run(startup(idea, investment))


if __name__ == '__main__':
    fire.Fire(main)
