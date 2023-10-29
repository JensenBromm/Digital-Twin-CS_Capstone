// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "CoreMinimal.h"
#include <mongocxx/instance.hpp>
#include <mongocxx/pool.hpp>

/**
 * 
 */
class ROBOTPROJ_API MongoInstance
{
private:
	mongocxx::instance dbInstance;
	std::unique_ptr<mongocxx::pool> clientPool;
	MongoInstance() {}

public:
	static MongoInstance* GetInstance()
	{
		static MongoInstance mongoInstance;
		return &mongoInstance;
	}

	//Create a pool object only once from the URI
	void createPool (std::string uri)
	{
		if (!clientPool)
		{
			clientPool = (std::unique_ptr<mongocxx::pool>) new mongocxx::pool {
				mongocxx::uri {uri}};
		}
	}

	//Acquire a client from the pool
	mongocxx::pool::entry getClientFromPool()
	{
		return clientPool->acquire();
	}
};
